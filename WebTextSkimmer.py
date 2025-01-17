import requests
from bs4 import BeautifulSoup

# Send a GET request to the webpage
url = 'https://www.patchvault.org/lodges'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the full text from the webpage
    full_text = soup.get_text()
    
    # Define the start and end markers
    start_marker = "Show No Known Issue Lodges (122)"
    end_marker = "©2013-2024 PatchVault®."
    
    # Extract the text between the markers
    start_index = full_text.find(start_marker)
    end_index = full_text.find(end_marker)
    
    if start_index != -1 and end_index != -1:
        # Adjust the start index to exclude the marker itself
        start_index += len(start_marker)
        extracted_text = full_text[start_index:end_index].strip()
        
        # Write the extracted text to a file
        with open('extracted_text.txt', 'w', encoding='utf-8') as file:
            file.write(extracted_text)
        
        print("The specific text has been written to 'extracted_text.txt'.")
    else:
        print("Markers not found in the text.")
else:
    print(f'Failed to retrieve the webpage. Status code: {response.status_code}')
