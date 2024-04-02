# Python Movie Rating System

## Description

Python Movie Rating System is a web application developed by Mohaimenul Islam using Django Rest Framework And As database i use SQLite3. It allows users to register, login, add movies, rate movies, and view details about movies along with their average ratings. The application implements an authentication system with email verification, ensuring that only authenticated users can create movie models and rate movies. Additionally, the application includes features such as pagination and search functionality for the movie model.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Sifathislam/Coding-Test-Invitation-from-Visionary-Tech-Solution.git
   ```

2. Navigate to the project directory:
   ```
   cd Coding-Test-Invitation-from-Visionary-Tech-Solution
   ```

3. Install basic dependencies:
   Please if need any other dependecies use requirement.txt(suggetion to use it)
   ```
   pip install django
   pip install djangorestframework
   pip install markdown      
   pip install django-filter
   pip install virtualenv
   pip install django-cors-headers
   pip install django-environ
   pip install django-email
   pip intall dj-database-url
   ```

5. Apply migrations:
   ```
   python manage.py migrate
   ```

6. Run the server:
   ```
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`

## Usage

1. **Register/Login:**
   - Use the provided API endpoints for registration and login:
     - Register: `http://127.0.0.1:8000/register/`
     - Login: `http://127.0.0.1:8000/login/`
   - Use the provided credentials for admin and normal user.
   - Admin username: admin
   - Admin password: 123
   - Normal user: Mohaimenul
   - Normal user Password : sifat123..

2. **Adding Movies:**
   - Authenticated users can add movies by making POST requests to the `movies` endpoint:
     - Endpoint: `http://127.0.0.1:8000/movies/`

3. **Viewing Movies:**
   - All users can view a list of all movies by making GET requests to the `movies` endpoint:
     - Endpoint: `http://127.0.0.1:8000/movies/`

4. **Rating Movies:**
   - Authenticated users can rate movies by making POST requests to the `ratings` endpoint:
     - Endpoint: `http://127.0.0.1:8000/ratings/`

5. **Search Movies:**
   - Users can search for a specific movie by making GET requests to the `movies` endpoint with a search query:
     - Endpoint: `http://127.0.0.1:8000/movies/?search=MovieName`

6. **View Movie Details with Average Rating:**
   - Users can view details about a specific movie along with its average rating by making a GET request to the movie's endpoint:
     - Endpoint: `http://127.0.0.1:8000/movies/{movie_id}`

7. **Pagination:**
   - Pagination is implemented for the movie list. Users can navigate through pages by specifying the page number in the request:
     - Example: `http://127.0.0.1:8000/movies/?page=2`

## Feedback

Your feedback is valuable. If you encounter any issues or have suggestions for improvement, please feel free to contact us at sifathislame790@gmail.com.

Thank you for using Python Movie Rating System!
Mohaimenul Islam
