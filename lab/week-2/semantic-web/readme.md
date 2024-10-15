
# Semantic Web Retrieval Project

**Course:** Information Retrieval and the Cloud (COMP 30039)

## Table of Contents

- [Semantic Web Retrieval Project](#semantic-web-retrieval-project)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Objectives](#objectives)
  - [Project Structure](#project-structure)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [Clone Repository](#clone-repository)
    - [Install Dependencies](#install-dependencies)
  - [NLTK Resources](#nltk-resources)
  - [Usage](#usage)
    - [1. Fetch HTML Content](#1-fetch-html-content)
    - [2. Text Preprocessing](#2-text-preprocessing)
    - [3. Semantic Analysis](#3-semantic-analysis)
  - [Running the Project](#running-the-project)
    - [Test Script](#test-script)
    - [Jupyter Notebook](#jupyter-notebook)
  - [Expected Output](#expected-output)
  - [Conclusion](#conclusion)
  - [Acknowledgments](#acknowledgments)

## Overview

The **Semantic Web Retrieval Project** showcases a Python-based system for semantic web retrieval, encompassing:

- **Web Scraping:** Extracts HTML content from targeted websites.
- **Parsing:** Utilizes BeautifulSoup for HTML parsing.
- **Text Preprocessing:** Prepares extracted text for analysis.
- **Semantic Analysis:** Employs NLTK to derive meaningful semantic relationships.

## Objectives

- **Web Scraping:** Master data extraction from web pages using BeautifulSoup.
- **Text Preprocessing:** Implement techniques to clean and prepare text data for analysis.
- **Semantic Analysis:** Analyze and extract relationships within text data using semantic tools.

## Project Structure

 python project structure & notebook jupyter

semantic_web/
├── python        # python project
  ├── store.py         # Stores information
  ├── retrieve.py      # Retrieves information
  ├── utils.py         # Text processing utilities
  ├── requirements.txt # Python package requirements
  ├── test.py          # Test script

├── notebook           # jupyter notebook
  ├── notebook.ipynb   # Jupyter notebook 

└── README.md        # Project documentation

## Installation

### Prerequisites

- Python 3.6 or later

### Clone Repository

```bash
git clone https://github.com/7kylor/semantic_web.git
cd semantic_web
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## NLTK Resources

Before running the project, download the necessary NLTK resources by executing the following in a Python shell:

```python
import nltk
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

Alternatively, ensure the download lines in `utils.py` are uncommented and run the script to fetch resources automatically.

## Usage

### 1. Fetch HTML Content

Retrieve HTML content from the specified URL and parse it using BeautifulSoup.

```python
url = "https://mec.edu.om/en/"
raw_text = fetch_website_content(url)
```

### 2. Text Preprocessing

Process the extracted text through the following steps:

- **Tokenization:** Split text into individual words.
- **Lowercasing:** Convert all tokens to lowercase.
- **Stop Words Removal:** Remove common non-informative words.
- **Lemmatization:** Reduce words to their base form.

```python
tokens = preprocess_text(raw_text)
store_information(url, tokens)
```

### 3. Semantic Analysis

Utilize WordNet to find synonyms for each token, enhancing semantic comprehension.

```python
query = "education technology"
results = search_database(query)
```

## Running the Project

You can execute the project using the test script or via a Jupyter Notebook.

### Test Script

Run the application by executing the `test.py` script:

```bash
python test.py
```

### Jupyter Notebook

1. Launch Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Create a new Python notebook.
3. Import code from `store.py`, `retrieve.py`, `utils.py`, and `test.py` into separate cells.
4. Run the cells sequentially to execute the project.

## Expected Output

After running the project, you should observe:

- **Fetched Content:** Structured display of the HTML content from the specified website.
- **Preprocessed Tokens:** A list of processed tokens (tokenized, lowercased, stop words removed, lemmatized).
- **Synonyms:** Synonyms for each token, illustrating semantic relationships.

Example:

```
Fetching content from: https://mec.edu.om/en/

Searching for: education technology
Matching URLs:
https://example.com/education-tech1
https://example.com/education-tech2
```

## Conclusion

The **Semantic Web Retrieval Project** integrates web scraping, text preprocessing, and semantic analysis to effectively extract and interpret information from web sources, demonstrating the practical application of these techniques in information retrieval.

## Acknowledgments

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [NLTK Documentation](https://www.nltk.org/)
- [Python Official Documentation](https://docs.python.org/3/)
