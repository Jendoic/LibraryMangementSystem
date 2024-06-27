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
  - `GET  /api/v1/lms/books/`: List all books.
  - `POST /api/v1/lms/books/`: Add a new book (librarian only).
  - `GET  /api/v1/lms/books/{id}/`: Retrieve a specific book.
  - `PUT  /api/v1/lms/books/{id}/`: Update a book (librarian only).
  - `DELETE /api/v1/lms/books/{id}/`: Delete a book (librarian only).

- **Users**:
  - `POST /api/v1/auth/signup`: Register a new user.
  - `GET /api/v1/auth/{id}/`: Retrieve a specific user profile.
  - `PUT /api/v1/auth/{id}/`: Update user profile.
  - `DELETE /api/v1/auth/{id}/`: Delete user profile.

- **Borrow Records**:
  - `GET  /api/v1/lms/borrowRecords/`: List all borrow records (librarian only).
  - `POST /api/v1/lms/borrowRecords/`: Borrow a book.
  - `GET  /api/v1/lms/borrowRecords{id}/`: Retrieve a specific borrow record.
  - `PUT  /api/v1/lms/borrowRecords{id}/`: Return a book.
  - `GET  /api/v1/lms/borrowRecords/overDue/`: Return all the record of book that are yet to be return (liberian only).


- **Categories**:
  - `GET  /api/v1/lms/categories/`: List all categories.
  - `POST /api/v1/lms/categories/`: Add a new category (librarian only).
  - `GET /api/v1/lms/categories/{id}/`: Retrieve a specific category.
  - `PUT /api/v1/lms/categories/{id}/`: Update a category (librarian only).
  - `DELETE /api/v1/lms/categories/{id}/`: Delete a category (librarian only).

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

- Access the API at `http://localhost/`.
- Use tools like Postman or cURL to interact with the API endpoints.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

