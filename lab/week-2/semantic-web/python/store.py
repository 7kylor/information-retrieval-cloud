import requests
from bs4 import BeautifulSoup
import sqlite3
from utils import preprocess_text

def fetch_website_content(url):
    """
    Fetches and parses the HTML content of a website.
    
    Args:
        url (str): The URL of the website to fetch.
        
    Returns:
        str: The extracted text content from the website.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

def store_information(url, tokens):
    """
    Stores the URL and its associated tokens into the SQLite database.
    
    Args:
        url (str): The URL of the website.
        tokens (list): A list of preprocessed tokens from the website.
    """
    # Connect to SQLite database (or create it)
    conn = sqlite3.connect('semantic_data.db')
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS website_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            tokens TEXT
        )
    ''')
    
    # Insert data
    tokens_str = ' '.join(tokens)  # Store tokens as a space-separated string
    try:
        cursor.execute('INSERT INTO website_data (url, tokens) VALUES (?, ?)', (url, tokens_str))
        conn.commit()
        print(f"Data stored for URL: {url}")
    except sqlite3.IntegrityError:
        print(f"URL already exists in the database: {url}")
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    url = "https://mec.edu.om/en/"
    raw_text = fetch_website_content(url)
    processed_tokens = preprocess_text(raw_text)
    store_information(url, processed_tokens)