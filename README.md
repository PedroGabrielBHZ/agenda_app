
# Agenda

Agenda is a simple web application built with Flask and htmx. It allows users to manage contacts and commitments.

## Features

- View a list of all contacts
- View a list of all commitments
- Add a new contact
- Add a new commitment
- Delete a contact
- Delete a commitment

## Installation

1. Clone the repository:

```sh
git clone <repository-url>
```

2. Navigate to the project directory:

```sh
cd <project-directory>
```

3. Install the required Python packages:

```sh
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:

```sh
flask run
```

2. Open a web browser and navigate to `http://127.0.0.1:5000`.

## Project Structure

- [`app.py`](command:_github.copilot.openRelativePath?%5B%22app.py%22%5D "app.py"): The main application file. It contains the Flask routes and logic for rendering templates and interacting with the database.
- [`db_manager.py`](command:_github.copilot.openRelativePath?%5B%22db_manager.py%22%5D "db_manager.py"): Contains functions for interacting with the database.
- [`db.json`](command:_github.copilot.openRelativePath?%5B%22db.json%22%5D "db.json"): The database file.
- [`templates/`](command:_github.copilot.openRelativePath?%5B%22templates%2F%22%5D "templates/"): Contains the HTML templates for the application.
- [`static/`](command:_github.copilot.openRelativePath?%5B%22static%2F%22%5D "static/"): Contains static files such as CSS and JavaScript files.
