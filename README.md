# User Account API

This repository provides a simple API for basic user account management, including account creation, user login, and fetching the list of registered users.

## Base URL

The base URL for the API is:

https://emprender-a3ir.onrender.com/api/v1


## Endpoints

### 1. Create Account

**Endpoint:**  
`POST /createAccount`

**Description:**  
This endpoint allows you to create a new user account.

**Request Headers:**  
- `Content-Type: application/json`

**Request Body:**
```json
{
  "username": "aditya",
  "password": "aditya@123"
}
```

### 2. Login

**Endpoint**
`POST /login`

**Description:**
This endpoint authenticates a user with the provided credentials.

**Request Headers:**

- `Content-Type: application/json`

**Request Body:**

```json
{
  "username": "aditya",
  "password": "aditya@123"
}
```


### 3. Get Registered Users
**Endpoint:**
`GET /login
`
**Description:**
This endpoint retrieves a list of all registered users.

**Sample Response:**
```json
[

{
    "username": "aditya",
    "password": "aditya@123"
  },
  {
    "username": "raja",
    "password": "raja@123"
  }

]
```
