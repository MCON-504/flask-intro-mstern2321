import requests
response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get('http://localhost:5000/about')
print(response.json())

response = requests.get('http://localhost:5000/greet/lila')
print(response.text)

response = requests.get('http://localhost:5000/calculate?num1=10&num2=5&operation=add')
print(response.json())

response = requests.get('http://localhost:5000/calculate?num1=10&num2=5&operation=divide')
print(response.json())

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(response.json(), response.status_code)

response = requests.post('http://localhost:5000/echo',
                         json = {"message" : "Hello"})
print(response.json())

response = requests.get('http://localhost:5000/status/404')
print(response.text, response.status_code)

response = requests.get('http://localhost:5000/status/401')
print(response.text, response.status_code)


response = requests.get('http://localhost:5000/about')
custom_header = response.headers.get('X-Custom-Header')
print(f"Custom Header: {custom_header}")

