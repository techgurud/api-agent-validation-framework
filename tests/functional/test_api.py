import requests
import pytest
from jsonschema import validate, ValidationError
import yaml
import os

# Load configuration
with open(os.path.join("config", "config.yaml"), 'r') as file:
    config = yaml.safe_load(file)

BASE_URL = config['base_url']

# Sample JSON schema for validating a user
user_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "username": {"type": "string"},
        "email": {"type": "string"},
    },
    "required": ["id", "name", "username", "email"]
}

# GET request example: Fetch users
def test_get_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200, "GET /users failed"
    
    users = response.json()
    assert isinstance(users, list), "Response is not a list"
    # Validate first user schema
    try:
        validate(instance=users[0], schema=user_schema)
    except ValidationError as e:
        pytest.fail(f"Schema validation error: {e}")

# POST request example: Create a new post
def test_create_post():
    payload = {"title": "Test Title", "body": "Test body", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201, "POST /posts failed"
    
    post = response.json()
    assert post.get("title") == payload["title"], "Mismatch in post title"

# PUT request example: Update a post
def test_update_post():
    payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=payload)
    assert response.status_code == 200, "PUT /posts/1 failed"
    
    post = response.json()
    assert post.get("title") == payload["title"], "Post update failed"

# DELETE request example: Delete a post
def test_delete_post():
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200, "DELETE /posts/1 failed"

# Negative testing: Access an invalid endpoint
def test_invalid_endpoint():
    response = requests.get(f"{BASE_URL}/invalid_endpoint")
    assert response.status_code == 404, "Invalid endpoint did not return 404"
