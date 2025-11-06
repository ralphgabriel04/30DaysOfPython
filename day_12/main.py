import string
import random
def random_user_id():
    alpha_num = string.ascii_letters + string.digits
    return ''.join(random.choices(alpha_num, k=6))
print(random_user_id())

def user_id_gen_by_user():
    number_of_char = int(input("Enter number of characters: "))
    number_of_ids = int(input("Enter number of IDs: "))
    alpha_num = string.ascii_letters + string.digits
    ids = [''.join(random.choices(alpha_num, k=number_of_char)) for _ in range(number_of_ids)]
    return "\n".join(ids)
print(user_id_gen_by_user())

def rgb_color_gen():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())

def list_of_hexa_colors(num):
    hex_colors = []
    for _ in range(num):
        colors = "#".join(random.choices("0123456789ABCDEF", k=6))
        hex_colors.append(f"#{colors}")
    return hex_colors
def list_of_rgb_colors(number):
    rgb_colors = []
    for _ in range(number):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb_colors.append(f"rgb({r},{g},{b})")
    return rgb_colors

def generate_colors(color_type, number):
    if color_type == "hexa":
        return list_of_hexa_colors(number)
    elif color_type == "rgb":
        return list_of_rgb_colors(number)
    else:
        return "Invalid color type"
print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))
print(generate_colors("rgb", 3))
print(generate_colors("rgb", 1))
