

import requests
import json

# 1. GET
response = requests.get(
    "https://jsonplaceholder.typicode.com/users/3",
)

# Request
print("\n" + "=" * 50 + "\n")
print("=== REQUEST ===")
print(f"Method: {response.request.method}")
print(f"URL:    {response.request.url}")
print(f"\nRequest Headers:")
for key, value in response.request.headers.items():
    print(f"  {key}: {value}")
print(f"\nRequest Body: {response.request.body}") 


# Response 
print("\\n=== RESPONSE ===")
print(f"Status: {response.status_code} {response.reason}")
print(f"\nResponse Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")
print(f"\nResponse Body:")
print(json.dumps(response.json(), indent=2))

# Elapsed Time
print(f"Total time: {response.elapsed.total_seconds():.3f} seconds")
print(f"That's {response.elapsed.total_seconds() * 1000:.0f} milliseconds")

print("\n" + "=" * 50 + "\n")

# 2. POST
response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "Request Anatomy Lab", "body": "Learning API request anatomy.", "userId": 1},
    headers={"X-Custom-Header": "learning-apis"}
)

# Request
print("=== REQUEST ===")
print(f"Method: {response.request.method}")
print(f"URL:    {response.request.url}")
print(f"\nRequest Headers:")
for key, value in response.request.headers.items():
    print(f"  {key}: {value}")
print(f"\nRequest Body: {response.request.body}") 


# Response 
print("\\n=== RESPONSE ===")
print(f"Status: {response.status_code} {response.reason}")
print(f"\nResponse Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")
print(f"\nResponse Body:")
print(json.dumps(response.json(), indent=2))

# Elapsed Time
print(f"Total time: {response.elapsed.total_seconds():.3f} seconds")
print(f"That's {response.elapsed.total_seconds() * 1000:.0f} milliseconds")

print("\n" + "=" * 50 + "\n")

# 3. PATCH
response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json={"title": "Anatomy Lab Assignment"},
    headers={"X-Custom-Header": "learning-apis"}
)

# Request
print("=== REQUEST ===")
print(f"Method: {response.request.method}")
print(f"URL:    {response.request.url}")
print(f"\nRequest Headers:")
for key, value in response.request.headers.items():
    print(f"  {key}: {value}")
print(f"\nRequest Body: {response.request.body}") 


# Response 
print("\\n=== RESPONSE ===")
print(f"Status: {response.status_code} {response.reason}")
print(f"\nResponse Headers:")
for key, value in response.headers.items():
    print(f"  {key}: {value}")
print(f"\nResponse Body:")
print(json.dumps(response.json(), indent=2))

# Elapsed Time
print(f"Total time: {response.elapsed.total_seconds():.3f} seconds")
print(f"That's {response.elapsed.total_seconds() * 1000:.0f} milliseconds")