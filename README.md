# Django Property Management

## Overview
This is a web-based property management system built with Django. It allows property owners and managers to efficiently handle properties, tenants, and leases.

## Features
- User authentication (Admin, Property Manager, Tenant)
- Property listing and management
- Tenant management
- Lease agreements tracking
- Payment tracking
- Maintenance request handling

## Installation
To run this project locally, follow these steps:

### Prerequisites
Make sure you have the following installed on your system:
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Steps
```sh
# Clone the repository
git clone https://github.com/xinyuwen23/django-property-management.git

# Navigate into the project directory
cd django-property-management

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create a superuser (follow the prompts)
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Open your browser and visit `http://127.0.0.1:8000/` to access the application.

## Usage
```md
- Log in as an admin, property manager, or tenant.
- Manage properties, tenants, and leases from the dashboard.
- Track payments and view financial reports.
- Handle maintenance requests efficiently.
```

## Technologies Used
```md
- Django (Backend Framework)
- SQLite / PostgreSQL (Database)
- HTML, CSS, JavaScript (Frontend)
- Bootstrap (Styling)
```

## Future Improvements
```md
- Implement automated rent payment processing
- Add support for multiple property owners
- Improve reporting and analytics features
- Enhance UI/UX for better user experience
```

## Contributing
```md
Feel free to submit issues or pull requests to improve this project!
```

---
**Author:** [Xinyu Wen](https://github.com/xinyuwen23)

