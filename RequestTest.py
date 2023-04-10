# import requests
# import json

# json_data = {'name': 'John', 'age': 30}
# json_data_str = json.dumps(json_data)
# url = 'https://sama123.pythonanywhere.com/process-json2'
# response = requests.post(url,json=json_data_str)
# print(response.text)

from PIL import Image

# Open the image file
for i in range(51):
    img = Image.open("path/to/{i}.jpg")

    # Convert the image to grayscale
    gray_img = img.convert("L")

    # Save the grayscale image
    gray_img.save("path/to/grayscale_image.jpg")