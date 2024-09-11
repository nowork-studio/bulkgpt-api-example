# BulkGPT API Documentation

## Overview

BulkGPT provides APIs to trigger bulk processing tasks and check their status. The following API documentation describes how to interact with the BulkGPT APIs to upload a CSV file for processing and to monitor the status of the task. The APIs use `POST` requests, and you must authenticate each request using your API key.

---

## 1. Upload Trigger API

### **Endpoint**

`POST https://api.bulkgpt.ai/upload-trigger`

### **Description**

This API is used to upload a CSV file in base64 format and trigger a bulk processing workflow.

### **Request**

#### **URL**

`https://api.bulkgpt.ai/upload-trigger`

#### **Headers**

| Key          | Value                    |
| ------------ | ------------------------ |
| x-api-key    | `<Your BulkGPT API Key>` |
| Content-Type | `application/json`       |

#### **Payload**

```json
{
	"workflowId": "v0#Workflow#<workflowId>#<timestamp>",
	"csvBase64": "<Base64 encoded CSV>"
}
```

-   `workflowId`: The ID of the workflow to trigger. You can find this ID from your BulkGPT dashboard.
-   `csvBase64`: A base64-encoded string of the CSV file content. Use the `encode_csv_to_base64()` function or similar to encode the file.

#### **Sample Payload**

```json
{
	"workflowId": "v0#Workflow#6b056f598d994d1ca98821cca221d07e#1721762149339",
	"csvBase64": "ZmlsZSBjb250ZW50IGhlcmU="
}
```

### **Response**

#### **Success Response**

```json
{
	"taskId": "MTcyNjAzNjU5M18yMDI0LTA5LTExLTA2OjM2OjMz"
}
```

#### **Error Response**

```json
{
	"error": "Invalid workflow ID or CSV file."
}
```

#### **Explanation**

-   `taskId`: A unique identifier for the task, which you can use to check the status of the bulk processing job. Use this `taskId` with the Status API.

---

## 2. Status API

### **Endpoint**

`POST https://api.bulkgpt.ai/status`

### **Description**

This API is used to retrieve the status of a task triggered by the Upload Trigger API.

### **Request**

#### **URL**

`https://api.bulkgpt.ai/status`

#### **Headers**

| Key          | Value                    |
| ------------ | ------------------------ |
| x-api-key    | `<Your BulkGPT API Key>` |
| Content-Type | `application/json`       |

#### **Payload**

```json
{
	"taskId": "<Task ID from the Upload Trigger API>"
}
```

#### **Sample Payload**

```json
{
	"taskId": "MTcyNjAzNjU5M18yMDI0LTA5LTExLTA2OjM2OjMz"
}
```

### **Response**

#### **Success Response**

```json
{
	"status": {
		"status": "completed",
		"numOfTasksCompleted": 24,
		"numOfTaskSuccess": 24,
		"totalNumOfTasks": 24,
		"downloadUrl": "https://example-bulkgpt-download-url.com"
	}
}
```

#### **Explanation**

-   `status.status`: Represents the current status of the task. Possible values:
    -   `preparing`: Task is being prepared.
    -   `inProgress`: Task is being processed.
    -   `finalizing`: Task is finalizing results.
    -   `completed`: Task has been completed.
    -   `error`: An error occurred during task processing.
    -   `canceled`: The task was canceled.
-   `status.numOfTasksCompleted`: The total number of tasks that have been processed (success or failure).
-   `status.numOfTaskSuccess`: The number of successfully completed tasks.
-   `status.totalNumOfTasks`: The total number of tasks that were expected to be processed.
-   `status.downloadUrl`: URL to download the result CSV file. This field is only available when the task status is `completed`.

#### **Error Response**

```json
{
	"error": "Invalid Task ID."
}
```

---

## Example Usage

1. **Upload CSV and Trigger a Workflow:**

    ```python
    response = requests.post(url="https://api.bulkgpt.ai/upload-trigger", json=payload, headers=headers)
    print(response.json())
    ```

2. **Check Status of a Task:**
    ```python
    response = requests.post(url="https://api.bulkgpt.ai/status", json=payload, headers=headers)
    print(response.json())
    ```

---

## Notes

-   Ensure that you have the correct `workflowId` before triggering the API.
-   The `csvBase64` must be a valid base64-encoded string of the CSV file content.
-   Use the `taskId` from the Upload Trigger API to check the status with the Status API.
