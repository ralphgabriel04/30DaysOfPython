"""
Day 29 - Building an API
=========================
30 Days of Python Challenge

RESTful API for managing 30DaysOfPython students
Implements CRUD operations (Create, Read, Update, Delete)
"""

from flask import Flask, Response, request, jsonify
import json
import os
import pymongo
from bson.objectid import ObjectId
from bson.json_util import dumps
from datetime import datetime
from urllib.parse import quote_plus

# Try to load from .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is optional

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# MongoDB Configuration
# Priority: 1. Environment variable MONGODB_URI, 2. Environment variable MONGODB_PASSWORD, 3. Default URI
MONGODB_USER = os.environ.get('MONGODB_USER', 'recrutementdisneyworldfr_db_user')
MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', '')
MONGODB_CLUSTER = os.environ.get('MONGODB_CLUSTER', '30dayofpython.38xt7ga.mongodb.net')
MONGODB_DB_NAME = os.environ.get('MONGODB_DB_NAME', 'thirty_days_of_python')

# Default MongoDB URI (can be overridden by environment variable)
DEFAULT_MONGODB_URI = 'mongodb+srv://recrutementdisneyworldfr_db_user:txnFnkv52hiOYtHx@30dayofpython.38xt7ga.mongodb.net/?appName=30DayOfPython'

# Build MongoDB URI
if os.environ.get('MONGODB_URI'):
    MONGODB_URI = os.environ.get('MONGODB_URI')
elif MONGODB_PASSWORD:
    encoded_password = quote_plus(MONGODB_PASSWORD)
    MONGODB_URI = f'mongodb+srv://{MONGODB_USER}:{encoded_password}@{MONGODB_CLUSTER}/?appName=30DayOfPython'
else:
    MONGODB_URI = DEFAULT_MONGODB_URI

# Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGODB_URI)
    client.admin.command('ping')
    db = client[MONGODB_DB_NAME]
    print(f"[OK] Connected to MongoDB: {MONGODB_DB_NAME}")
except Exception as e:
    print(f"[ERROR] Failed to connect to MongoDB: {e}")
    db = None


def json_response(data, status_code=200):
    """Helper function to return JSON response"""
    return Response(
        dumps(data),
        mimetype='application/json',
        status=status_code
    )


@app.route('/api/v1.0/students', methods=['GET'])
def get_all_students():
    """
    GET /api/v1.0/students
    Retrieve all students from the database
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        students = list(db.students.find())
        return json_response(students)
    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/students/<id>', methods=['GET'])
def get_student_by_id(id):
    """
    GET /api/v1.0/students/<id>
    Retrieve a single student by ID
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        if not ObjectId.is_valid(id):
            return json_response({'error': 'Invalid student ID format'}, 400)

        student = db.students.find_one({'_id': ObjectId(id)})

        if student:
            return json_response(student)
        else:
            return json_response({'error': 'Student not found'}, 404)
    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    """
    POST /api/v1.0/students
    Create a new student

    Expected form data or JSON:
    - name: string (required)
    - country: string (required)
    - city: string (required)
    - birthyear: string (required)
    - skills: string (comma-separated, optional)
    - bio: string (optional)
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        # Get data from request (supports both form data and JSON)
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Validate required fields
        required_fields = ['name', 'country', 'city', 'birthyear']
        missing_fields = [field for field in required_fields if field not in data or not data[field]]

        if missing_fields:
            return json_response({
                'error': f'Missing required fields: {", ".join(missing_fields)}'
            }, 400)

        # Process skills (convert comma-separated string to list if needed)
        skills = []
        if 'skills' in data and data['skills']:
            if isinstance(data['skills'], str):
                skills = [skill.strip() for skill in data['skills'].split(',')]
            elif isinstance(data['skills'], list):
                skills = data['skills']

        # Create student document
        student = {
            'name': data['name'],
            'country': data['country'],
            'city': data['city'],
            'birthyear': data['birthyear'],
            'skills': skills,
            'bio': data.get('bio', ''),
            'created_at': datetime.now()
        }

        # Insert into database
        result = db.students.insert_one(student)
        student['_id'] = result.inserted_id

        return json_response({
            'message': 'Student created successfully',
            'student': student
        }, 201)

    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    """
    PUT /api/v1.0/students/<id>
    Update an existing student

    Expected form data or JSON (all fields optional):
    - name: string
    - country: string
    - city: string
    - birthyear: string
    - skills: string (comma-separated) or list
    - bio: string
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        if not ObjectId.is_valid(id):
            return json_response({'error': 'Invalid student ID format'}, 400)

        # Check if student exists
        existing_student = db.students.find_one({'_id': ObjectId(id)})
        if not existing_student:
            return json_response({'error': 'Student not found'}, 404)

        # Get data from request
        if request.is_json:
            data = request.get_json()
        else:
            data = request.form.to_dict()

        # Build update document (only include fields that are provided)
        update_data = {}

        if 'name' in data:
            update_data['name'] = data['name']
        if 'country' in data:
            update_data['country'] = data['country']
        if 'city' in data:
            update_data['city'] = data['city']
        if 'birthyear' in data:
            update_data['birthyear'] = data['birthyear']
        if 'bio' in data:
            update_data['bio'] = data['bio']
        if 'skills' in data:
            if isinstance(data['skills'], str):
                update_data['skills'] = [skill.strip() for skill in data['skills'].split(',')]
            elif isinstance(data['skills'], list):
                update_data['skills'] = data['skills']

        # Add updated_at timestamp
        update_data['updated_at'] = datetime.now()

        if not update_data:
            return json_response({'error': 'No fields to update'}, 400)

        # Update the student
        query = {"_id": ObjectId(id)}
        db.students.update_one(query, {"$set": update_data})

        # Get updated student
        updated_student = db.students.find_one({'_id': ObjectId(id)})

        return json_response({
            'message': 'Student updated successfully',
            'student': updated_student
        })

    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    """
    DELETE /api/v1.0/students/<id>
    Delete a student by ID
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        if not ObjectId.is_valid(id):
            return json_response({'error': 'Invalid student ID format'}, 400)

        # Check if student exists
        student = db.students.find_one({'_id': ObjectId(id)})
        if not student:
            return json_response({'error': 'Student not found'}, 404)

        # Delete the student
        result = db.students.delete_one({"_id": ObjectId(id)})

        if result.deleted_count > 0:
            return json_response({
                'message': 'Student deleted successfully',
                'deleted_id': id
            })
        else:
            return json_response({'error': 'Failed to delete student'}, 500)

    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/students', methods=['DELETE'])
def delete_all_students():
    """
    DELETE /api/v1.0/students
    Delete all students (use with caution!)
    """
    if db is None:
        return json_response({'error': 'Database connection failed'}, 500)

    try:
        result = db.students.delete_many({})
        return json_response({
            'message': f'Deleted {result.deleted_count} student(s)',
            'deleted_count': result.deleted_count
        })
    except Exception as e:
        return json_response({'error': str(e)}, 500)


@app.route('/api/v1.0/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return json_response({
        'status': 'healthy',
        'database': 'connected' if db is not None else 'disconnected',
        'timestamp': datetime.now().isoformat()
    })


@app.route('/', methods=['GET'])
def index():
    """API documentation endpoint"""
    return json_response({
        'message': '30DaysOfPython Students API',
        'version': '1.0',
        'endpoints': {
            'GET /api/v1.0/students': 'Get all students',
            'GET /api/v1.0/students/<id>': 'Get student by ID',
            'POST /api/v1.0/students': 'Create a new student',
            'PUT /api/v1.0/students/<id>': 'Update a student',
            'DELETE /api/v1.0/students/<id>': 'Delete a student',
            'GET /api/v1.0/health': 'Health check'
        },
        'example_student': {
            'name': 'John Doe',
            'country': 'USA',
            'city': 'New York',
            'birthyear': '1990',
            'skills': ['Python', 'Flask', 'MongoDB'],
            'bio': 'A passionate Python developer'
        }
    })


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print(f"\n{'='*60}")
    print("30DaysOfPython Students API")
    print(f"{'='*60}")
    print(f"Server running on http://localhost:{port}")
    print(f"API Base URL: http://localhost:{port}/api/v1.0")
    print(f"{'='*60}\n")
    app.run(debug=True, host='0.0.0.0', port=port)
