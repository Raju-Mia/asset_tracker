# Corporate Assets Management System

The Corporate Assets Management System is a Django application designed to track corporate assets such as phones, tablets, laptops, and other equipment assigned to employees.

---

## Getting Started

These instructions will guide on how to set up and run the Corporate Assets Management System on your local machine.

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Database system (SQLite)

### Installation

1. Clone the repository or download the ZIP file and extract its contents.

2. To create a virtual environment and activate it, you can follow these steps:

- python -m venv myenv
- source env/bin/activate (for- macOS/Linux).
- .\myenv\Scripts\activate or myenv/Scripts/activate (For- Windows).

3. Install the required dependencies by running the following command:

- pip install -r requirements.txt

4. Apply the database migrations to create the necessary tables and schema:

- python manage.py makemigrations
- python manage.py migrate

5. Create a superuser account to access the admin interface:

- python manage.py createsuperuser

### Run the Application

6. Start the development server by running the following command:

- python manage.py runserver

7. Access the application in your web browser at- `http://localhost:8000/`.

## API Endpoints

You can access the API endpoints using a tool like cURL, Postman, or a web browser. Here are the available endpoints:

- Companies: `http://localhost:8000/api/companies/`
- Employees: `http://localhost:8000/api/employees/`
- Devices: `http://localhost:8000/api/devices/`
- Device Logs: `http://localhost:8000/api/logs/`

### Project Structure info-

- project name: 'asset_tracker'
- App name: 'asset_management'

---

Feel free to customize and enhance the project to fit your specific requirements. If you have any questions or need further assistance, please don't hesitate to reach out.

### Thank You --- RAJU MIA
