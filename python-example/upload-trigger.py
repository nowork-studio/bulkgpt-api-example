import base64
import requests

# Use encode_csv_to_base64 function to encode your csv to base64 string
def encode_csv_to_base64(file_path):
    with open(file_path, "rb") as file:
        csv_content = file.read()
    encoded_content = base64.b64encode(csv_content).decode('utf-8')
    return encoded_content

url = "https://api.bulkgpt.ai/upload-trigger"

payload = {
    "workflowId": "v0#Workflow#6b056f598d994d1ca98821cca221d07e#1721762149339", 
    "csvBase64": encode_csv_to_base64(file_path="./input.csv")
}

headers = {
    "x-api-key": "<Your BulkGPT API Key>",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
"""
Output Example:
{
    'taskId': 'MTcyNjAzNjU5M18yMDI0LTA5LTExLTA2OjM2OjMz'
}

Explaination:
    taskId: You will be getting the status, progress and download url by providing this taskId the status API, see status API documentation
"""