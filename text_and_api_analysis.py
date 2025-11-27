"""
Text and API Analysis Tasks
- Analyze Romeo and Juliet word frequencies
- Analyze cats API data (weights, lifespans, countries)
- Analyze countries API data (largest countries, languages)
- Scrape UCI datasets page
"""

import re
import json
from collections import Counter
from statistics import mean, median, stdev

# Try to use requests library, fall back to urllib if not available
try:
    import requests
    USE_REQUESTS = True
except ImportError:
    from urllib import request
    USE_REQUESTS = False

def clean_text(text):
    """Remove punctuation and convert to lowercase"""
    # Remove non-alphabetic characters and convert to lowercase
    words = re.findall(r'\b[a-z]+\b', text.lower())
    return words

def analyze_romeo_juliet():
    """Fetch Romeo and Juliet and find 10 most frequent words"""
    print("=" * 60)
    print("ROMEO AND JULIET - WORD FREQUENCY ANALYSIS")
    print("=" * 60)

    urls = [
        'https://www.gutenberg.org/files/1112/1112.txt',
        'http://www.gutenberg.org/files/1112/1112.txt',
        'https://www.gutenberg.org/cache/epub/1112/pg1112.txt'
    ]

    text = None
    for url in urls:
        try:
            print(f"Trying URL: {url}")
            if USE_REQUESTS:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                text = response.text
            else:
                with request.urlopen(url, timeout=10) as response:
                    text = response.read().decode('utf-8')
            print(f"✓ Successfully fetched text ({len(text)} characters)")
            break
        except Exception as e:
            print(f"✗ Failed: {e}")
            continue

    if not text:
        print("ERROR: Could not fetch Romeo and Juliet text from any URL")
        return

    # Clean and count words
    words = clean_text(text)
    word_counts = Counter(words)

    # Get top 10 most frequent words
    top_10 = word_counts.most_common(10)

    print(f"\nTotal words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")
    print("\nTop 10 Most Frequent Words:")
    print("-" * 40)
    for i, (word, count) in enumerate(top_10, 1):
        print(f"{i:2}. {word:15} - {count:5} occurrences")
    print()

def analyze_cats_api():
    """Fetch and analyze cats API data"""
    print("=" * 60)
    print("CATS API ANALYSIS")
    print("=" * 60)

    try:
        url = 'https://api.thecatapi.com/v1/breeds'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        if USE_REQUESTS:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            cats_data = response.json()
        else:
            req = request.Request(url, headers=headers)
            with request.urlopen(req, timeout=10) as response:
                cats_data = json.loads(response.read().decode('utf-8'))

        print(f"✓ Fetched data for {len(cats_data)} cat breeds\n")

        # Extract weight data (metric)
        weights = []
        for cat in cats_data:
            if 'weight' in cat and 'metric' in cat['weight']:
                weight_range = cat['weight']['metric']
                # Parse weight range like "3 - 5" or "4 - 6"
                parts = weight_range.split('-')
                if len(parts) == 2:
                    try:
                        min_w = float(parts[0].strip())
                        max_w = float(parts[1].strip())
                        avg_weight = (min_w + max_w) / 2
                        weights.append(avg_weight)
                    except:
                        pass

        # Extract lifespan data
        lifespans = []
        for cat in cats_data:
            if 'life_span' in cat:
                lifespan_range = cat['life_span']
                # Parse lifespan like "14 - 15" or "12 - 15"
                parts = lifespan_range.split('-')
                if len(parts) == 2:
                    try:
                        min_l = float(parts[0].strip())
                        max_l = float(parts[1].strip())
                        avg_lifespan = (min_l + max_l) / 2
                        lifespans.append(avg_lifespan)
                    except:
                        pass

        # Weight statistics
        print("CAT WEIGHT STATISTICS (Metric - kg)")
        print("-" * 40)
        if weights:
            print(f"Min:              {min(weights):.2f} kg")
            print(f"Max:              {max(weights):.2f} kg")
            print(f"Mean:             {mean(weights):.2f} kg")
            print(f"Median:           {median(weights):.2f} kg")
            if len(weights) > 1:
                print(f"Std Deviation:    {stdev(weights):.2f} kg")
        print()

        # Lifespan statistics
        print("CAT LIFESPAN STATISTICS (years)")
        print("-" * 40)
        if lifespans:
            print(f"Min:              {min(lifespans):.2f} years")
            print(f"Max:              {max(lifespans):.2f} years")
            print(f"Mean:             {mean(lifespans):.2f} years")
            print(f"Median:           {median(lifespans):.2f} years")
            if len(lifespans) > 1:
                print(f"Std Deviation:    {stdev(lifespans):.2f} years")
        print()

        # Country-Breed frequency table
        print("FREQUENCY TABLE: CAT BREEDS BY COUNTRY")
        print("-" * 40)
        country_breeds = {}
        for cat in cats_data:
            country = cat.get('origin', 'Unknown')
            breed = cat.get('name', 'Unknown')
            if country not in country_breeds:
                country_breeds[country] = []
            country_breeds[country].append(breed)

        # Sort by number of breeds (descending)
        sorted_countries = sorted(country_breeds.items(),
                                 key=lambda x: len(x[1]),
                                 reverse=True)

        for country, breeds in sorted_countries[:15]:  # Top 15 countries
            print(f"{country:20} - {len(breeds):2} breeds: {', '.join(breeds[:3])}" +
                  (f"..." if len(breeds) > 3 else ""))
        print()

    except Exception as e:
        print(f"ERROR: Failed to fetch cats API data: {e}\n")

def analyze_countries_api():
    """Fetch and analyze countries API data"""
    print("=" * 60)
    print("COUNTRIES API ANALYSIS")
    print("=" * 60)

    try:
        # Try multiple REST countries API endpoints
        # v3.1 API requires fields parameter
        urls = [
            'https://restcountries.com/v3.1/all?fields=name,area,languages',
            'https://restcountries.com/v2/all',
            'https://restcountries.eu/rest/v2/all'
        ]

        countries_data = None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        for url in urls:
            try:
                print(f"Trying countries API: {url}")
                if USE_REQUESTS:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    countries_data = response.json()
                else:
                    req = request.Request(url, headers=headers)
                    with request.urlopen(req, timeout=10) as response:
                        countries_data = json.loads(response.read().decode('utf-8'))
                break
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                continue

        if not countries_data:
            print("ERROR: Could not fetch countries data from any API")
            return

        print(f"✓ Fetched data for {len(countries_data)} countries\n")

        # Determine API version based on data structure
        api_version = 'v3' if isinstance(countries_data[0].get('name'), dict) else 'v2'
        print(f"Using API version: {api_version}\n")

        # 10 Largest countries by area
        print("10 LARGEST COUNTRIES (by area)")
        print("-" * 40)

        if api_version == 'v3':
            countries_with_area = [
                (c.get('name', {}).get('common', 'Unknown'), c.get('area', 0))
                for c in countries_data if 'area' in c
            ]
        else:  # v2
            countries_with_area = [
                (c.get('name', 'Unknown'), c.get('area', 0))
                for c in countries_data if 'area' in c
            ]

        largest_countries = sorted(countries_with_area,
                                  key=lambda x: x[1],
                                  reverse=True)[:10]

        for i, (country, area) in enumerate(largest_countries, 1):
            print(f"{i:2}. {country:30} - {area:15,.0f} km²")
        print()

        # 10 Most spoken languages
        print("10 MOST SPOKEN LANGUAGES")
        print("-" * 40)
        language_count = Counter()
        all_languages = set()

        for country in countries_data:
            if 'languages' in country and country['languages']:
                langs = country['languages']
                if isinstance(langs, dict):
                    langs = langs.values()
                elif isinstance(langs, list):
                    # Already a list
                    pass
                else:
                    continue

                for lang in langs:
                    if lang:  # Skip None/empty values
                        language_count[lang] += 1
                        all_languages.add(lang)

        most_spoken = language_count.most_common(10)
        for i, (language, count) in enumerate(most_spoken, 1):
            print(f"{i:2}. {language:30} - {count:3} countries")
        print()

        # Total number of languages
        print(f"TOTAL LANGUAGES: {len(all_languages)} unique languages")
        print()

    except Exception as e:
        print(f"ERROR: Failed to fetch countries API data: {e}\n")

def scrape_uci_datasets():
    """Scrape UCI datasets page using BeautifulSoup4"""
    print("=" * 60)
    print("UCI DATASETS PAGE SCRAPING")
    print("=" * 60)

    try:
        # Check if BeautifulSoup4 is available
        try:
            from bs4 import BeautifulSoup
        except ImportError:
            print("WARNING: BeautifulSoup4 not installed")
            print("Install with: pip install beautifulsoup4")
            print("\nAttempting basic scraping without BeautifulSoup...")

            url = 'https://archive.ics.uci.edu'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }

            if USE_REQUESTS:
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                html = response.text
            else:
                req = request.Request(url, headers=headers)
                with request.urlopen(req, timeout=10) as response:
                    html = response.read().decode('utf-8', errors='ignore')

            print(f"✓ Fetched page ({len(html)} characters)")
            print("\nWithout BeautifulSoup, parsing is limited.")
            print("Here's a sample of the raw HTML:")
            print("-" * 40)
            print(html[:500])
            print("...")
            return

        # With BeautifulSoup - try multiple URLs as UCI site has changed
        urls = [
            'https://archive.ics.uci.edu',
            'https://archive.ics.uci.edu/datasets',
            'https://archive.ics.uci.edu/ml/datasets.php'
        ]

        html = None
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        for url in urls:
            try:
                print(f"Trying UCI URL: {url}")
                if USE_REQUESTS:
                    response = requests.get(url, headers=headers, timeout=10)
                    response.raise_for_status()
                    html = response.text
                else:
                    req = request.Request(url, headers=headers)
                    with request.urlopen(req, timeout=10) as response:
                        html = response.read().decode('utf-8', errors='ignore')
                print(f"  ✓ Success!")
                break
            except Exception as e:
                print(f"  ✗ Failed: {e}")
                continue

        if not html:
            print("ERROR: Could not fetch UCI page")
            return

        soup = BeautifulSoup(html, 'html.parser')
        print(f"\n✓ Fetched and parsed page with BeautifulSoup ({len(html)} characters)\n")

        # Try to find dataset information
        # Look for links to datasets
        dataset_links = soup.find_all('a', href=True)
        dataset_count = 0
        print("Sample dataset links found:")
        print("-" * 40)
        for link in dataset_links[:20]:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            if 'dataset' in href.lower() or 'data' in text.lower():
                if text and len(text) > 3:
                    print(f"  • {text[:50]}")
                    dataset_count += 1
                    if dataset_count >= 10:
                        break

        # Try to find tables
        tables = soup.find_all('table')
        if tables:
            print(f"\nFound {len(tables)} table(s) on the page")
            print("\nFirst table preview:")
            print("-" * 40)
            first_table = tables[0]
            rows = first_table.find_all('tr')[:5]
            for row in rows:
                cells = row.find_all(['td', 'th'])
                row_text = ' | '.join(cell.get_text(strip=True)[:30] for cell in cells)
                if row_text:
                    print(row_text[:100])

    except Exception as e:
        print(f"ERROR: Failed to scrape UCI page: {e}\n")

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("TEXT AND API ANALYSIS - 30 Days of Python")
    print("=" * 60 + "\n")

    # Run all analyses
    analyze_romeo_juliet()
    analyze_cats_api()
    analyze_countries_api()
    scrape_uci_datasets()

    print("=" * 60)
    print("ANALYSIS COMPLETE")
    print("=" * 60)
