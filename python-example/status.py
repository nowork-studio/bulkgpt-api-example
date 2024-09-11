import requests

url = "https://api.bulkgpt.ai/status"

payload = {
    "taskId": "MTcyNjAzNjU5M18yMDI0LTA5LTExLTA2OjM2OjMz"
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
    'status': {
        'status': 'completed', 
        'numOfTasksCompleted': 24, 
        'numOfTaskSuccess': 24, 
        'totalNumOfTasks': 24, 
        'downloadUrl': 'https://example-bulkgpt-download-url.com"
    }
}

Explaination:
    status.status: "preparing" | "inProgress" | "finalizing" | "completed" | "error" | "canceled"
    status.totalNumOfTasks: Optional, representing the total number of tasks
    status.numOfTaskSuccess: Optional, representing total number of tasks succeeded
    status.numOfTasksCompleted: Optional, representing total number of tasks succeeded and failed
    status.downloadUrl: Optional, only available when status value is "completed", representing the output.csv download url
"""
