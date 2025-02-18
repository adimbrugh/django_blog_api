📌 API Documentation Structure
1️⃣ Authentication APIs

🔹 Register User
Method: POST
Endpoint: /api/auth/register/
Body (JSON):

json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "securepassword123"
}
Response (201 Created):

json
{
  "message": "User registered successfully!",
  "user_id": 1
}


🔹 Login User
Method: POST
Endpoint: /api/auth/login/
Body (JSON):

json
{
  "username": "testuser",
  "password": "securepassword123"
}
Response (200 OK):

json
{
  "token": "your_access_token_here"
}




2️⃣ Blog Post APIs
🔹 Create a Post
Method: POST
Endpoint: /api/posts/
Headers: Authorization: Token your_access_token_here
Body (JSON):

json
{
  "title": "My First Blog Post",
  "content": "This is the content of the post",
  "tags": ["django", "blog"]
}
Response (201 Created):

json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of the post",
  "tags": ["django", "blog"],
  "created_at": "2025-02-17T12:00:00Z"
}


🔹 Retrieve All Posts
Method: GET
Endpoint: /api/posts/
Response (200 OK):

json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of the post",
    "tags": ["django", "blog"]
  }
]


🔹 Retrieve a Single Post
Method: GET
Endpoint: /api/posts/1/
Response (200 OK):

json
{
  "id": 1,
  "title": "My First Blog Post",
  "content": "This is the content of the post",
  "tags": ["django", "blog"]
}


🔹 Update a Post
Method: PUT
Endpoint: /api/posts/1/
Headers: Authorization: Token your_access_token_here
Body (JSON):

json
{
  "title": "Updated Blog Post",
  "content": "Updated content",
  "tags": ["django", "webdev"]
}
Response (200 OK):

json
{
  "id": 1,
  "title": "Updated Blog Post",
  "content": "Updated content",
  "tags": ["django", "webdev"]
}


🔹 Delete a Post
Method: DELETE
Endpoint: /api/posts/1/
Headers: Authorization: Token your_access_token_here
Response (204 No Content)




3️⃣ Comment APIs
🔹 Create a Comment
Method: POST
Endpoint: /api/posts/1/comments/
Headers: Authorization: Token your_access_token_here
Body (JSON):

json
{
  "content": "This is my comment on the post"
}
Response (201 Created):

json
{
  "id": 1,
  "post": 1,
  "author": "testuser",
  "content": "This is my comment on the post",
  "created_at": "2025-02-17T12:05:00Z"
}
🔹 Retrieve Comments for a Post
Method: GET
Endpoint: /api/posts/1/comments/
Response (200 OK):

json
[
  {
    "id": 1,
    "author": "testuser",
    "content": "This is my comment on the post",
    "created_at": "2025-02-17T12:05:00Z"
  }
]
🔹 Update a Comment
Method: PUT
Endpoint: /api/posts/1/comments/1/
Headers: Authorization: Token your_access_token_here
Body (JSON):

json
{
  "content": "Updated comment"
}
Response (200 OK):

json
{
  "id": 1,
  "content": "Updated comment"
}


🔹 Delete a Comment
Method: DELETE
Endpoint: /api/posts/1/comments/1/
Headers: Authorization: Token your_access_token_here
Response (204 No Content)




4️⃣ Tagging & Search APIs
🔹 Get Posts by Tag
Method: GET
Endpoint: /api/tags/django/
Response (200 OK):
json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of the post",
    "tags": ["django", "blog"]
  }
]


🔹 Search Posts
Method: GET
Endpoint: /api/posts/search/?q=django
Response (200 OK):
json
[
  {
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the content of the post",
    "tags": ["django", "blog"]
  }
]



📌 Export & Share Postman Documentation
Once you've added these requests in Postman, follow these steps to generate online API documentation:
1-Open Postman and select your API collection.
2-Click on "Export" (three-dot menu) → "Generate API Documentation".
3-Click "Publish" and copy the Postman Documentation URL.


🚀 Summary
✅ Covers all blog features (Auth, Posts, Comments, Tags, Search).
✅ Uses best practices (DRF, authentication, structured endpoints).
✅ Easy to import into Postman for testing.
✅ Generates shareable API documentation.