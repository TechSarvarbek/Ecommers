import requests

# Yaratish uchun POST so'rovi
create_url = 'http://127.0.0.1:8000/api/product/products/'
headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE4MTExMTgyLCJpYXQiOjE3MTgxMTA4ODIsImp0aSI6IjM5Mzk0ZTFmYjUwZTQwOTg5NWNjMzFjZWM5NjhhNDE0IiwidXNlcl9pZCI6OH0.LWz4NPpg2e4kLeU9Nvwtk314yy5BbH-cMmi-yPOch4Y'}
data = {
    'title': 'Acer Notebook',
    'description': 'Product Description',
    'deliver': 'true',
    'price': '9.99',
}
files = [
    ('images', ('images.jpg', open(r'C:\Users\user\Documents\Ecommers\backend\images.jpg', 'rb'), 'image/jpeg')),
    # ('images', ('image2.jpg', open('path/to/image2.jpg', 'rb'), 'image/jpeg')),
    # ...
]
response = requests.post(create_url, headers=headers, data=data, files=files)
if response.status_code == 201:
    print('Product created successfully!')
    product_id = response.json()['id']
else:
    print('Failed to create product.')
    print(response.json())

