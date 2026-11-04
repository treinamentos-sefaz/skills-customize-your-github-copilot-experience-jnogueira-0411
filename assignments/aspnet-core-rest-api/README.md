# 📘 Assignment: First REST API with ASP.NET Core

## 🎯 Objective

Build a beginner-friendly REST API in C# with ASP.NET Core Minimal APIs. Create endpoints to check the service, list in-memory tasks, and add a task using JSON.

## 📝 Tasks

### 🛠️ Create and Run a Minimal API

#### Descrição
Create a new web project with the .NET CLI and add a health endpoint to its `Program.cs` file. Run the application and open the endpoint using the local URL printed by `dotnet run`.

#### Requisitos
O programa concluído deve:

- Create the project with `dotnet new web -n TodoApi`
- Start successfully with `dotnet run`
- Return HTTP `200 OK` and `{"status":"ok"}` from `GET /health`


### 🛠️ List In-Memory Tasks

#### Descrição
Define a `TodoItem` record and create a list in memory with at least one task. Add an endpoint that returns the current list as JSON.

#### Requisitos
O programa concluído deve:

- Represent each task with an integer ID, a title, and a completion status
- Store tasks in a collection in memory without using a database
- Return the collection from `GET /todos` as a JSON array


### 🛠️ Add a Task with a POST Request

#### Descrição
Create a request model that accepts a task title and add a `POST /todos` endpoint. The endpoint should assign a new ID, store the task, and return the created task.

#### Requisitos
O programa concluído deve:

- Accept a JSON request body containing a non-empty `title`
- Add the new task to the in-memory collection with a unique integer ID
- Return HTTP `201 Created` with the created task in the response
- Show the new task in the results of a later `GET /todos` request

Example request body:

```json
{
  "title": "Review Minimal APIs"
}
```