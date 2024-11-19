# Task Manager API

A task management application built with Django and Django REST Framework that allows users to create, update, delete, and mark tasks as completed. The API is protected using token-based authentication to ensure that only authorized users can interact with the tasks.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [API Endpoints](#api-endpoints)
  - [Create Task](#create-task)
  - [Get All Tasks](#get-all-tasks)
  - [Get Task Details](#get-task-details)
  - [Update Task](#update-task)
  - [Delete Task](#delete-task)
  - [Mark Task Complete](#mark-task-complete)
- [task.json](#taskjson)
- [Running Tests](#running-tests)
- [Contributing](#contributing)

## Features

- User authentication using **Token-based authentication**.
- CRUD operations for tasks:
  - Create new tasks
  - Retrieve all tasks
  - Retrieve task details
  - Update existing tasks
  - Delete tasks
  - Mark tasks as complete
- Secure API with user authentication required for all actions.
  
## Technologies Used

- **Backend Framework**: Django
- **Django REST Framework**: For building the API
- **Authentication**: Token-based Authentication
- **Database**: SQLite (default, can be switched to PostgreSQL or MySQL)
- **Testing**: Django’s test framework, with DRF’s APIClient

## Setup Instructions

### Prerequisites

Before running the application, make sure you have the following installed:
- Python 3.x
- Django
- Django REST Framework
- SQLite (default, should work out of the box)

### 1. Clone the repository

```bash
git clone https://github.com/Phanisharan/task_manager.git
cd task_manager
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Apply migrations

Run the following command to set up the database and apply migrations:

```bash
python manage.py migrate
```

### 4. Create a superuser

To access the Django admin and manage users, create a superuser:

```bash
python manage.py createsuperuser
```

### 5. Run the server

To start the development server:

```bash
python manage.py runserver
```

Your API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

### Create Task
- **POST** `/tasks/create/`
- **Description**: Create a new task
- **Authentication**: Token required
- **Request Body**:
```json
{
  "title": "Test Task",
  "description": "A sample task for testing",
  "due_date": "2024-11-25",
  "status": "pending"
}
```
- **Response**: Returns the created task object with a 201 status.

### Get All Tasks
- **GET** `/tasks/`
- **Description**: Retrieve all tasks
- **Authentication**: Token required
- **Response**: A list of task objects.

### Get Task Details
- **GET** `/tasks/{id}/`
- **Description**: Retrieve the details of a single task by ID
- **Authentication**: Token required
- **Response**: A single task object.

### Update Task
- **PUT** `/tasks/{id}/`
- **Description**: Update an existing task by ID
- **Authentication**: Token required
- **Request Body**:
```json
{
  "title": "Updated Task",
  "description": "Updated task description",
  "due_date": "2024-11-30",
  "status": "in-progress"
}
```
- **Response**: Returns the updated task object.

### Delete Task
- **DELETE** `/tasks/{id}/`
- **Description**: Delete a task by ID
- **Authentication**: Token required
- **Response**: A success message with a 204 status.

### Mark Task Complete
- **PATCH** `/tasks/complete/{id}/`
- **Description**: Mark a task as completed by ID
- **Authentication**: Token required
- **Response**: Returns the task object with the status updated to "completed".

## task.json

The `task.json` file contains initial task data for testing purposes. This file can be used to pre-populate the database with tasks.

### Example `task.json`

```json
[
    {
        "id": "cd5a97e8-6b1c-4d4f-9a74-ae2f0d3b9b72",
        "title": "Deploy Application",
        "description": "Deploy the latest version of the application to the production server.",
        "due_date": "2024-12-03",
        "status": "pending"
    },
    {
        "id": "de6f24a9-7e2b-45c1-a8c5-bf5e0d9c6d34",
        "title": "Organize Workshop",
        "description": "Plan and organize a technical workshop for the team.",
        "due_date": "2024-12-04",
        "status": "pending"
    }
]
```

### How to Use `task.json`

1. **Loading Tasks**: You can load the tasks from `task.json` into your database using the following custom Django management command:
   
   Create a management command by placing the following script in `task_manager/management/commands/load_tasks_from_json.py`:

```python
from django.core.management.base import BaseCommand
import json
from task_manager.models import Task

class Command(BaseCommand):
    help = 'Load tasks from a JSON file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file'], 'r') as file:
            tasks_data = json.load(file)
            for task in tasks_data:
                Task.objects.create(**task)
            self.stdout.write(self.style.SUCCESS('Successfully loaded tasks from JSON file'))
```

2. **Run the command**:
   
```bash
python manage.py load_tasks_from_json task.json
```

This will read the data from `task.json` and populate the database with tasks.

## Running Tests

You can run the tests to ensure everything is working as expected:

```bash
python manage.py test task_manager
```

This will run all the test cases in your application, including the API tests for task creation, task updates, and more.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a branch, and submit a pull request with your changes. Make sure to add tests for any new features or bug fixes.




