# Django Bookstore Project

## Setup (Docker)
- `docker-compose up -d`: to create a container with web and database services
- `docker-compose exec web python3 manage.py migrate`: to run migrations
- `docker-compose exec web python3 manage.py createsuperuser`: to create django admin user
- `docker-compose exec web pytest` to run tests
- `docker-compose logs` to check logs (email console)
- `docker-compose down`: to remove all containers

## Routes
- /accounts/signup/ - Register new user
- /accounts/login/ - Log in user
- /admin - Create books and reviews
- /books - List books (protected). Add permission 'Can read all books' in django admin
- /books/\<uuid\> - Show book details
- /books/search/?q=foo - Search books by title __or__ author

## Auth Features
This project uses __django-allauth__ package that provides urls for signup, login, logout, change password, email verification and more.
