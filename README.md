
# File Manager Service

A fast and secure file manager service built with FastAPI.

## Features

- Upload files with validation and size limits.
- Download files securely.
- Delete files.
- Retrieve file details.
- Supports concurrent uploads.
- Dockerized for easy deployment.
- Uses MySQL as the database.
- Centralized configuration for URLs and settings.
- Middleware for database session management.

## Technologies Used

- **FastAPI**: High-performance web framework.
- **Uvicorn**: ASGI server for FastAPI.
- **SQLAlchemy**: ORM for database interactions.
- **Alembic**: Database migrations.
- **Pydantic**: Data validation.
- **PyTest**: Testing framework.
- **Docker**: Containerization.
- **MySQL**: Database.
- **Python-Magic**: For MIME type detection.

## Project Structure

```plaintext
file_manager_service/
├── alembic/
│   └── versions/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   ├── utils.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── upload.py
│   │   │   ├── download.py
│   │   │   ├── delete.py
│   │   │   └── details.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── security.py
│   │   └── urls.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── meta.py
│   │   ├── tables.py
│   │   └── driver.py
│   └── tests/
│       ├── __init__.py
│       └── test_api.py
├── .env
├── alembic.ini
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Docker and Docker Compose installed.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/javadasoodeh/file-manager.git
   cd file-manager
   ```

2. **Create a .env file:**

   ```bash
   touch .env
   ```

3. Populate it with:

   ```env
   DATABASE_URL=mysql+mysqlconnector://user:password@db:3306/file_manager
   MAX_UPLOAD_SIZE_MB=100
   STORAGE_PATH=./storage/
   ```

   Note: Replace user, password, and other details with your actual database credentials.

4. **Build and run the Docker containers:**

   ```bash
   docker-compose up --build
   ```

5. **Apply database migrations:**

   ```bash
   docker-compose exec web alembic upgrade head
   ```

6. **Access the API documentation:**

   Navigate to http://localhost:8000/docs to view the interactive API documentation.

## API Endpoints

1. **Upload File**
   - URL: `/upload`
   - Method: `POST`
   - Form Data:
     - `file`: The file to upload.
   - Response:
     ```json
     {
       "file_id": "generated-file-id",
       "size": 12345,
       "name": "original-filename.pdf"
     }
     ```

2. **Download File**
   - URL: `/download/{file_id}`
   - Method: `GET`
   - Response:
     - Returns the file as a downloadable response.

3. **Delete File**
   - URL: `/delete`
   - Method: `POST`
   - JSON Body:
     ```json
     {
       "file_id": "file-id-to-delete"
     }
     ```
   - Response:
     ```json
     {
       "message": "File deleted successfully."
     }
     ```

4. **Get File Details**
   - URL: `/details`
   - Method: `POST`
   - JSON Body:
     ```json
     {
       "files": ["file-id-1", "file-id-2"]
     }
     ```
   - Response:
     ```json
     [
       {
         "file_id": "file-id-1",
         "name": "filename1.pdf",
         "size": 12345,
         "extension": "pdf",
         "content_type": "application/pdf"
       },
       {
         "file_id": "file-id-2",
         "name": "filename2.pdf",
         "size": 67890,
         "extension": "pdf",
         "content_type": "application/pdf"
       }
     ]
     ```

## Running Tests

### Install dependencies:

If not using Docker, create a virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

### Run tests:

```bash
pytest
```

## Configuration

Configuration is managed via environment variables in the .env file.

- `DATABASE_URL`: Database connection string.
- `MAX_UPLOAD_SIZE_MB`: Maximum allowed file upload size in megabytes.
- `STORAGE_PATH`: Directory where uploaded files are stored.

## Database Migrations

Database migrations are handled using Alembic.

### Initialize Alembic (if not already initialized):

```bash
alembic init alembic
```

### Create a migration script:

```bash
alembic revision --autogenerate -m "Create files table"
```

### Apply migrations:

```bash
alembic upgrade head
```

## Project Details

### Middleware for Database Session
- The application uses middleware to manage the database session.
- The session is attached to `request.state.db` and is accessible in all route handlers without needing to declare it as a dependency.
- This approach ensures that the database session is created and closed per request, avoiding repetition and potential leaks.

### Centralized URLs
- All route URLs are defined in `app/core/urls.py`.
- This centralization avoids hard-coded URLs in the route definitions and makes it easier to manage and update routes.

### File Validation
- Uses `python-magic` to validate the MIME type of uploaded files.
- Allowed file types are specified in `app/core/config.py` under `ALLOWED_FILE_TYPES`.

### Error Handling
- The application includes error handling for common scenarios, such as file size limits, invalid file types, and missing files.

## Security Considerations

- **File Validation**: Ensures that only allowed file types are accepted.
- **Size Limits**: Enforces maximum upload size to prevent abuse.
- **Database Security**: Use environment variables for sensitive information like database credentials.
- **Dependencies**: Keep dependencies up to date to mitigate vulnerabilities.

## Additional Notes

- **Database Migrations with Alembic**

  - Update `alembic.ini` to use the MySQL connection string.

    ```ini
    # alembic.ini
    [alembic]
    script_location = alembic
    sqlalchemy.url = mysql+mysqldb://user:password@db:3306/file_manager
    ```


  - Create initial migration:

    ```bash
    alembic revision --autogenerate -m "Create files table"
    ```

  - Apply migrations:

    ```bash
    alembic upgrade head
    ```

- **Docker MySQL Configuration**

  - The `docker-compose.yml` uses the official MySQL 8.0 image.
  - Environment variables are set for the MySQL database.
  - Ports are mapped to allow external connections if needed.

- **Dependencies**

  - **mysqlclient** is used for MySQL support in SQLAlchemy.
  - Ensure you have the necessary build tools installed to compile `mysqlclient` if not using Docker.

- **Testing**

  - Update tests if necessary to accommodate any changes due to the switch to MySQL.
  - Ensure the test database is correctly configured.

## License

This project is licensed under the MIT License.

## Contact

For issues or contributions, please create an issue or pull request on GitHub.
