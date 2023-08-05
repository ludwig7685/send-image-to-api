import requests

# Replace with the actual URL of your Flask app
app_url = "URL OF YOUR WEBSITE"

# Specify the path to the image file you want to send
image_path = "/home/container/1.png"

# Send the POST request to the API endpoint
response = requests.post(f"{app_url}/api/generate_caption", files={'image': open(image_path, 'rb')})

# Check if the request was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    image_name = data['image_name']
    description = data['description']

    print(f"Image Name: {image_name}")
    print(f"Description: {description}")
else:
    print(f"Error: {response.text}")
