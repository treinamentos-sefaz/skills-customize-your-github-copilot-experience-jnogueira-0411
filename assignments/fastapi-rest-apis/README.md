# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API in Python using FastAPI. Practice defining endpoints, validating request data with Pydantic, and implementing CRUD operations with appropriate HTTP responses.

## 📝 Tasks

### 🛠️ Create the API and a Health Endpoint

#### Descrição
Use the provided starter code to run a FastAPI application. Add a `GET /health` endpoint that confirms the service is running, then inspect the automatically generated API documentation.

#### Requisitos
O programa concluído deve:

- Install the dependencies with `python -m pip install fastapi uvicorn`
- Start locally with `uvicorn main:app --reload`
- Return a JSON response such as `{"status": "ok"}` from `GET /health`
- Serve interactive API documentation at `/docs`


### 🛠️ Create and List Books

#### Descrição
Use the `BookCreate` and `Book` models to implement endpoints for adding books to the in-memory collection and listing all books.

#### Requisitos
O programa concluído deve:

- Accept a book's `title` and `author` as validated JSON input
- Create books with unique integer IDs and return HTTP status `201`
- Return all saved books from `GET /books`, including an empty list when there are none

Example request:

```json
{
  "title": "The Hobbit",
  "author": "J. R. R. Tolkien"
}
```


### 🛠️ Complete Book CRUD Operations

#### Descrição
Add endpoints to retrieve, update, and delete an individual book by ID. Return a clear `404 Not Found` response when the requested ID does not exist.

#### Requisitos
O programa concluído deve:

- Retrieve a book with `GET /books/{book_id}`
- Update a book with `PUT /books/{book_id}` and return the updated book
- Delete a book with `DELETE /books/{book_id}` and return an appropriate success response
- Use FastAPI's `HTTPException` to report missing books with status `404`