from store import fetch_website_content, store_information
from retrieve import search_database
from utils import preprocess_text

def main():
    # Step 1: Store Information
    url = "https://mec.edu.om/en/"
    print(f"Fetching content from: {url}")
    raw_text = fetch_website_content(url)
    tokens = preprocess_text(raw_text)
    store_information(url, tokens)
    
    # Step 2: Retrieve Information
    query = "education technology"
    print(f"\nSearching for: {query}")
    results = search_database(query)
    if results:
        print("Matching URLs:")
        for res in results:
            print(res)
    else:
        print("No matching URLs found.")

if __name__ == "__main__":
    main()