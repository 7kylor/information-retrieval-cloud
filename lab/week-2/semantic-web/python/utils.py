import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Ensure NLTK resources are downloaded
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """
    Preprocesses the input text by tokenizing, removing stop words, and lemmatizing.
    
    Args:
        text (str): The raw text to preprocess.
        
    Returns:
        list: A list of processed tokens.
    """
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Convert to lowercase and remove non-alphabetic tokens
    tokens = [token.lower() for token in tokens if token.isalpha()]
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    return tokens