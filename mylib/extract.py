"""
Extract a dataset from a URL like Kaggle or data.gov. 
JSON or CSV formats tend to work well

food dataset
"""
import requests

def extract(url="https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv", 
            file_path="airline.csv"):
    """Extract a raw CSV file from a URL to a local file path"""
    response = requests.get(url)
    response.raise_for_status()  # Check for any request issues
    
    with open(file_path, 'wb') as f:
        f.write(response.content)
    return file_path




