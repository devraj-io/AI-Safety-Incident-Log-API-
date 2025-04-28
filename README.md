# AI Safety Incident Log API

This project is a Django-based REST API for logging and managing AI safety incidents. It allows users to create, retrieve, and delete incidents, providing a structured way to track and analyze AI-related safety issues.

## Features

- **Incident Management**: Create, retrieve, and delete incidents.
- **Severity Levels**: Incidents can be categorized as `Low`, `Medium`, or `High` severity.
- **RESTful API**: Built using Django REST Framework for easy integration with other systems.
- **Database Seeding**: Preload the database with sample incidents using a custom management command.

## Project Structure
myproject/ ├── db.sqlite3 # SQLite database file ├── manage.py # Django management script ├── README.md # Project documentation ├── incidents/ # App for managing incidents │ ├── models.py # Incident model definition │ ├── serializers.py # Serializers for API data validation │ ├── views.py # API views for handling requests │ ├── urls.py # URL routing for the incidents app │ ├── tests.py # Unit tests for the app │ ├── migrations/ # Database migrations │ ├── management/ # Custom management commands │ └── admin.py # Admin interface configuration └── myproject/ # Project configuration ├── settings.py # Project settings ├── urls.py # Root URL configuration ├── wsgi.py # WSGI entry point └── asgi.py # ASGI entry point


## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

2. Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```

pip install -r requirements.txt
```
4. Apply database migrations:
```
python manage.py migrate
```
5. Seed the database with sample data:
```
python manage.py seed
```
6. Start the development server:
```
python manage.py runserver
```
API Endpoints
```
Method	Endpoint	Description
GET	/incidents	Retrieve all incidents
POST	/incidents	Create a new incident
GET	/incidents/<id>	Retrieve a specific incident
DELETE	/incidents/<id>	Delete a specific incident
```

Example Incident Object:
```
{
  "id": 1,
  "title": "AI system misidentification",
  "description": "An AI facial recognition misidentified a person.",
  "severity": "High",
  "reported_at": "2025-04-24T13:40:00Z"
}
```
Running Tests
Run the following command to execute the test suite:
```
python [manage.py](http://_vscodecontentref_/14) test
```
Contributing
Contributions are welcome! Please fork the repository and submit a pull request.
