import requests
import json

def fetch_and_search():
    # Ask for user input
    search_term = input("Enter company name to search: ")
    
    # URL of the JSON file
    url = "https://raw.githubusercontent.com/duckduckgo/tracker-radar/refs/heads/main/build-data/generated/entity_map.json"
    
    try:
        # Fetch the JSON data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        
        # Search for the company in the JSON data
        found = False
        for company, info in data.items():
            if company.lower().startswith(search_term.lower()):
                # Create text file with the company name
                filename = f"{search_term}.txt"
                with open(filename, 'w') as f:
                    # Write all properties (domains) to the file
                    for domain in info['properties']:
                        f.write(domain + '\n')
                
                print(f"File '{filename}' has been created with the following domains:")
                print('\n'.join(info['properties']))
                found = True
                break
        
        if not found:
            print(f"No company found matching '{search_term}'")
                
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_and_search()