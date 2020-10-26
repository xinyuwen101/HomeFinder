# HomeFinder

A real estate property management system for rental properties.

Implemented with Python, Django, HTML, CSS, JavaScript, Bootstrap and Postgres.

Deployed to Oracle IaaS with an Ubuntu server using Docker as the container platform, Nginx and uWSGI as the web servers to improve performance.

Link: http://hf.xinyuwen.me

## Features

* Developed Home, Property Listings, and Property Details pages.
* Built a property uploading page that allows users to add a new property.
* Built a search page that allows users to search for properties by address, city, state, zipcode or other features.
* Built a Contact system that allows users to send message to a property's owner.
* Implemented User Authentication and Email Notification.
* Implemented Internationalization (i18n) that allows users to change languages between English and Chinese.


## How to install

```sh
pip install -r requirements.txt

python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```