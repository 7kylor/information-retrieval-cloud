import sqlite3
from nltk.corpus import wordnet
from utils import preprocess_text

def get_synonyms(word):
    """
    Retrieves synonyms for a given word using WordNet.
    
    Args:
        word (str): The word to find synonyms for.
        
    Returns:
        set: A set of synonyms.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms

def search_database(query):
    """
    Searches the SQLite database for entries matching the query or its synonyms.
    
    Args:
        query (str): The search query.
        
    Returns:
        list: A list of URLs that match the query.
    """
    # Preprocess the query
    tokens = preprocess_text(query)
    
    # Expand query with synonyms
    expanded_terms = set(tokens)
    for token in tokens:
        synonyms = get_synonyms(token)
        expanded_terms.update(synonyms)
    
    # Connect to the database
    conn = sqlite3.connect('semantic_data.db')
    cursor = conn.cursor()
    
    # Search for matching tokens
    placeholders = ' OR '.join(['tokens LIKE ?' for _ in expanded_terms])
    sql_query = f"SELECT url FROM website_data WHERE {placeholders}"
    
    # Prepare parameters with wildcards
    params = [f"%{term}%" for term in expanded_terms]
    
    cursor.execute(sql_query, params)
    results = cursor.fetchall()
    
    # Close connection
    conn.close()
    
    # Extract URLs from results
    urls = [result[0] for result in results]
    return urls

if __name__ == "__main__":
    search_query = "education technology"
    matching_urls = search_database(search_query)
    print(f"URLs matching the query '{search_query}':")
    for url in matching_urls:
        print(url)