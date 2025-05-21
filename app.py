import requests
import json

API_Key = "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"
API = "https://api.groq.com/openai/v1/models"

headers  ={
    "Authorization":f"Bearer {API_Key}",
    "Content-Type":"application/json"
}
payload ={
    "model":""
}
response = requests.request("GET",API,headers=headers)
print(response.content)
Hallo