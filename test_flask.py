import pytest
import requests

def test_hello():
  response = requests.get('http://localhost:5000')
  assert response.status_code == 200
  assert response.text == 'Hello, World'
