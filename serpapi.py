import os
import requests

# List of codes to search
codes = ["Replace with actual codes"]

# Create a folder to save images
output_folder = 'downloaded_images'
os.makedirs(output_folder, exist_ok=True)

# SerpApi configuration
api_key = 'Replace with your SerpApi key'
api_url = 'https://serpapi.com/search'

for code in codes:
    # Set up parameters for the API request
    params = {
        'q': code,
        'tbm': 'isch',  # Image search
        'api_key': api_key
    }

    # Make the API request
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        # Check if there are image results
        if 'images_results' in data and len(data['images_results']) > 0:
            first_image = data['images_results'][0]
            image_url = first_image['original']  # Get the original image URL

            # Download the image
            image_response = requests.get(image_url)
            if image_response.status_code == 200:
                # Create the filename
                filename = f"{code}-00.jpg"
                file_path = os.path.join(output_folder, filename)

                # Save the image
                with open(file_path, 'wb') as file:
                    file.write(image_response.content)
                    print(f"Downloaded: {file_path}")
            else:
                print(f"Failed to download image for '{code}'. Status code: {image_response.status_code}")
        else:
            print(f"No images found for '{code}'.")
    else:
        print(f"Failed to fetch results for '{code}'. Status code: {response.status_code}")

# Output the list of downloaded images
print("Image download process completed.")
