# Library Management System

Welcome to the Library Management System, an API built with Django REST Framework to manage library operations such as cataloging books, managing user accounts, and handling book borrowing and returning processes.

## Features

- **Book Catalog Management**:
  - Add, update, delete, and view books.
  - Categorize books by genres and authors.
  - Search and filter books by title, author, or category.

- **User Management**:
  - User registration and authentication.
  - Manage user profiles.
  - Differentiate between regular users and librarians.

- **Borrowing and Returning Books**:
  - Borrow available books and track borrowing records.
  - Return books and update the borrowing status.
  - Track due dates and notify users about overdue books.

- **Permissions and Access Control**:
  - Ensure only librarians can manage book records.
  - Users can view and borrow books.
  - Users can view their own borrowing history.
  - Librarians can view all borrowing records.

## Data Models

- **Book**:
  - `title`, `author`, `isbn`, `published_date`, `category`, `available_copies`.

- **User**:
  - `username`, `email`, `password`, `is_librarian`.

- **BorrowRecord**:
  - `user`, `book`, `borrow_date`, `due_date`, `return_date`.

- **Category**:
  - `name`.

## API Endpoints

- **Books**:
  - `GET /books/`: List all books.
  - `POST /books/`: Add a new book (librarian only).
  - `GET /books/{id}/`: Retrieve a specific book.
  - `PUT /books/{id}/`: Update a book (librarian only).
  - `DELETE /books/{id}/`: Delete a book (librarian only).

- **Users**:
  - `POST /users/`: Register a new user.
  - `GET /users/{id}/`: Retrieve a specific user profile.
  - `PUT /users/{id}/`: Update user profile.
  - `DELETE /users/{id}/`: Delete user profile.

- **Borrow Records**:
  - `GET /borrow-records/`: List all borrow records (librarian only).
  - `POST /borrow-records/`: Borrow a book.
  - `GET /borrow-records/{id}/`: Retrieve a specific borrow record.
  - `PUT /borrow-records/{id}/`: Return a book.

- **Categories**:
  - `GET /categories/`: List all categories.
  - `POST /categories/`: Add a new category (librarian only).
  - `GET /categories/{id}/`: Retrieve a specific category.
  - `PUT /categories/{id}/`: Update a category (librarian only).
  - `DELETE /categories/{id}/`: Delete a category (librarian only).

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/library-management-system.git
    cd library-management-system
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

### Usage

- Access the API at `http://127.0.0.1:8000/`.
- Use tools like Postman or cURL to interact with the API endpoints.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

