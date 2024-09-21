# Social Media API

This project is a simple Social Media API built with Django and Django REST Framework (DRF), implementing user authentication using custom user models and token authentication.

## Features
- User Registration with custom fields (`bio`, `profile_picture`, `followers`)
- User Login with token generation
- Token-based authentication for secure API access

## Installation

### Prerequisites
- Python 3.x
- Django 3.x or higher
- Django REST Framework
- Django REST Framework Token Authentication

### Setup Instructions

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd social_media_api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    If there’s no `requirements.txt` file, you can manually install the dependencies:

    ```bash
    pip install django djangorestframework djangorestframework-simplejwt
    ```

4. **Set up the database and migrate:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser (optional, for admin access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### 1. **User Registration**

   - **URL:** `/api/accounts/register/`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
         "username": "your_username",
         "password": "your_password",
         "bio": "Your bio",
         "profile_picture": "path/to/profile/picture.jpg"
     }
     ```
   - **Response:**
     ```json
     {
         "token": "generated_token"
     }
     ```

### 2. **User Login**

   - **URL:** `/api/accounts/login/`
   - **Method:** `POST`
   - **Request Body:**
     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```
   - **Response:**
     ```json
     {
         "token": "generated_token"
     }
     ```

### 3. **User Profile**

   - **URL:** `/api/accounts/profile/`
   - **Method:** `GET`
   - **Headers:**
     ```http
     Authorization: Token your_generated_token
     ```
   - **Response:**
     ```json
     {
         "username": "your_username",
         "bio": "Your bio",
         "profile_picture": "url/to/profile/picture.jpg",
         "followers": ["follower1", "follower2"]
     }
     ```

## Testing the API

You can use tools like [Postman](https://www.postman.com/) or [cURL](https://curl.se/) to test the API endpoints.

### Example Postman Usage:

1. **User Registration:**
   - URL: `http://127.0.0.1:8000/api/accounts/register/`
   - Method: `POST`
   - Body: `raw` JSON:
     ```json
     {
         "username": "testuser",
         "password": "testpassword",
         "bio": "Test user bio"
     }
     ```

2. **User Login:**
   - URL: `http://127.0.0.1:8000/api/accounts/login/`
   - Method: `POST`
   - Body: `raw` JSON:
     ```json
     {
         "username": "testuser",
         "password": "testpassword"
     }
     ```

3. **View User Profile (Authenticated):**
   - URL: `http://127.0.0.1:8000/api/accounts/profile/`
   - Method: `GET`
   - Headers:
     ```
     Authorization: Token <your_token_here>
     ```

## Custom User Model

The project uses a custom user model that extends `AbstractUser` and includes the following additional fields:
- **bio**: A text field for the user's biography
- **profile_picture**: An optional image field for profile pictures
- **followers**: A ManyToMany field for user followers (symmetrical=False)

Make sure to update the `AUTH_USER_MODEL` in `settings.py`:

```python
AUTH_USER_MODEL = 'accounts.CustomUser'



## API Endpoints

### Posts
- `GET /api/posts/`: List all posts.
- `POST /api/posts/`: Create a new post (requires authentication).
- `GET /api/posts/{id}/`: Retrieve a specific post.
- `PUT /api/posts/{id}/`: Update a post (owner only).
- `DELETE /api/posts/{id}/`: Delete a post (owner only).

### Comments
- `GET /api/comments/`: List all comments.
- `POST /api/comments/`: Create a new comment (requires authentication).

