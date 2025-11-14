import requests
import json

response = requests.post("http://localhost:3000/add-overlay", json={
    "imageUrl": "https://picsum.photos/800/800",
    "title": "Teste",
    "category": "SUPLEMENTOS",
    "config": {
        "colors": {
            "SUPLEMENTOS": ""
        }
    }
})

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
