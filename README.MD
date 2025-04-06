## 🧠 What is the requests module?
The requests module is a Python library used to send HTTP requests like:

* GET (fetch data)

* POST (send data)

* PUT (update data)

* DELETE (remove data)

It’s like a bridge between your Python script and any website or REST API.

### For Practice website
```
https://reqres.in/
```

To install:

```sh
pip install requests
```

## 🧠 What are headers in a requests call?
Headers are key-value pairs sent in an HTTP request (or response) to provide meta-information about the request or the client.

Think of headers as:

* 👤 Identity cards (who's making the request?)

* 📦 Format hints (what kind of data is being sent/received?)

* 🔐 Security tokens (is the request authorized?)

## 🔧 Common Use Cases for Headers
### 1. Content-Type
Tells the server what type of data you are sending.

```
headers = {
    'Content-Type': 'application/json'
}
```

### 2. Authorization
Used for APIs that require authentication (e.g., Bearer tokens, Basic Auth).

```
headers = {
    'Authorization': 'Bearer <your_token>'
}
```

### 3. User-Agent
Identifies the client (browser, tool, etc.).

```
headers = {
    'User-Agent': 'my-awesome-script/1.0'
}
```
🧪 Example
```
import requests

url = "https://api.example.com/data"

headers = {
    'Authorization': 'Bearer my_secret_token',
    'Content-Type': 'application/json',
    'User-Agent': 'kalyan-devops-script/1.0'
}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

## 🌐 URL and URL Parameters in Python `requests`

---

### 🔗 What is a URL?

**URL (Uniform Resource Locator)** is the web address of the resource you want to access.

**Example:**


This URL will return a list of all posts from the fake JSON API.

---

### 🧩 What are URL Parameters (also called Query Parameters)?

URL parameters are extra data passed in the URL to filter or modify the response from the server.

**Example:**


```
https://jsonplaceholder.typicode.com/posts?userId=1
```

```
This fetches all posts where `userId` is 1.

The format is:
```
<base_url>?key1=value1&key2=value2

```

---

### 🛠️ Using Parameters in `requests.get()`

Instead of manually building the query string, use the `params` argument:

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId': 1}

response = requests.get(url, params=params)

print("Final URL:", response.url)
print("Data:", response.json())

```

## ✅ Output

```
Final URL: https://jsonplaceholder.typicode.com/posts?userId=1
Data: [ { post1... }, { post2... } ]

```

## 🔍 Pro Tip
You can pass multiple parameters like this:

```
params = {
    'userId': 1,
    'sort': 'asc',
    'limit': 10
}
```
The URL becomes:

```
...?userId=1&sort=asc&limit=10
```

## 📤 Sending JSON Data in a POST Request using `requests`

---

### 📌 Use Case

You often need to send JSON data to an API—for example, submitting a form, creating a resource, or sending configuration data.

---

### 🧪 Example: Sending JSON using `requests.post()`

```python
import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "DevOps with Python",
    "body": "Learning to send JSON data using requests module.",
    "userId": 100
}

response = requests.post(url, json=payload)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
```

## ⚠️ Important Notes
* Use json=payload to automatically:

    * Convert Python dictionary to JSON

    * Set Content-Type: application/json header

* Do not manually encode with json.dumps() unless you're also setting headers manually.

## ✅ Summary Table

| Parameter | Purpose                   | Used With | Example Value                             |
|-----------|----------------------------|-----------|--------------------------------------------|
| `params`  | Add query params to URL    | GET       | `{'id': 1}` → `?id=1`                      |
| `json`    | Send JSON body             | POST/PUT  | `{'title': 'Hello'}`                       |
| `data`    | Send form/raw body         | POST/PUT  | `'username=admin&password=123'`           |
| `headers` | Custom request headers     | All       | `{'Authorization': 'Bearer token'}`       |


## ✅ HTTP Methods Summary Table

| Method  | Purpose                          | Request Type | Body Support | Example Use Case                                  |
|---------|----------------------------------|---------------|--------------|---------------------------------------------------|
| `GET`   | Retrieve data from the server    | Safe/Idempotent | ❌ No       | Fetch user info, list resources                   |
| `POST`  | Send data to create a resource   | Non-idempotent | ✅ Yes      | Create a new user, submit a form                  |
| `PUT`   | Replace an existing resource     | Idempotent     | ✅ Yes      | Update a full user profile                        |
| `PATCH` | Partially update a resource      | Non-idempotent | ✅ Yes      | Update a single field like `email`               |
| `DELETE`| Delete a resource from server    | Idempotent     | ✅ Optional | Remove a user or delete a file                    |
| `HEAD`  | Same as GET, but no response body| Safe/Idempotent | ❌ No       | Check if a resource exists                        |
| `OPTIONS`| Returns allowed HTTP methods    | Safe           | ❌ No       | Preflight check in CORS requests                  |

---

### ✅ Notes:

- **Safe**: Does not change server state (`GET`, `HEAD`, `OPTIONS`)
- **Idempotent**: Repeating the same request yields the same result (`GET`, `PUT`, `DELETE`)
- **Non-idempotent**: Repeating may create multiple resources or have different effects (`POST`, `PATCH`)

---

## 🖼️ Sending Files or Images with Python `requests`

You can send any file (text, image, etc.) using the `files` parameter in a POST request.

---

### 📂 1. Upload a File (e.g., `.txt` or `.log`)

```python
import requests

url = "https://httpbin.org/post"
file_path = "sample.txt"

with open(file_path, 'rb') as f:
    files = {'file': f}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())
```

### 🖼️ 2. Upload an Image (e.g., .jpg, .png)

```python
import requests

url = "https://httpbin.org/post"
image_path = "image.png"

with open(image_path, 'rb') as img:
    files = {'image': ('image.png', img, 'image/png')}
    response = requests.post(url, files=files)

print(response.status_code)
print(response.json())

```
## 🧪 Real Use Cases 
* Upload logs to APIs (e.g., Jira, ServiceNow)

* Send screenshots in automation reports

* Push zipped backups or configs to remote APIs


## ⏱️ Setting Timeouts in Python `requests`

Use the `timeout` parameter to specify how long (in seconds) to wait for:

- **Connection timeout** – time to establish a connection
- **Read timeout** – time to wait for the server to send data

---

### 🧪 Example: Simple Timeout

```python
import requests

url = "https://httpbin.org/delay/5"  # Delays response by 5 seconds

try:
    response = requests.get(url, timeout=3)  # Timeout set to 3 seconds
    print(response.status_code)
except requests.exceptions.Timeout:
    print("⏰ Request timed out!")
```

### ⚙️ Specify (connect_timeout, read_timeout)
```python
response = requests.get(url, timeout=(2, 5))
# 2 sec to connect, 5 sec to read response
```