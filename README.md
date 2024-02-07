# Bookworm Bookstore
## _A Django-based web app. Implements Django templates and PostgreSQL as a Database._

The project is divided into the following apps for better project structure:

- Account : Hold One-to-one relation with the User. A signal is implemented to create an Account, once a User is created. Holds details about the user.  
- Blog: Contains the implementation of the Article model.
- Bookworm_auth: Registration, Authentication, and Authorization of users.
- Bookstore: Core functionality of the bookstore. CRUD over Book, Author, Category
- Cart: Adding Books to the Cart, allowing the follow-up checkout.
- Core: Contains common functionality for the project. Including Permissions, Mixins, and others.

## Authentication
The website allows the user to register an account and profile. The app extends the Django build-in User to provide login with only an email
The user can  add book items to a personal wishlist and add Books to a cart.

## Authorization
A superuser can mark registered users as Staff and add them to a Staff group, giving them additional privileges to perform CRUD operations over Book, Author, Article, and Category models.

In the project are implemented CBVs, as well as function views. The templates are provided from ThemeForest and modified to Django templates using the build-in functionality to extend code 
