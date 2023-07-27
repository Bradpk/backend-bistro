Description

For this project, we will be creating a simple Python/Django API to serve as the backend for our previously created React Restaurant frontend app. 
Create the models, views, and database for an API that provides READ operations for a user’s restaurant items in a PostgresQL database. 

MoSCoW 

MUST: 

1: The following data in your PostgreSQL database and implement models for READ only operations for the following data:
Menu Items
Title
Description
Price
Spicy Level
FK to Category
FK to Cuisine
Category (Appetizer, Dessert, Main Dish, etc.)
Cuisine (American, Thai, etc.)

2: Views to send JSON data back to a GET request for a list of all menu items with the category and cuisine labels nested in the data.

3: Routes to use the views created in the previous step.

4: The Changed URL in the React Restaurant Project Repo. 


SHOULD: 

1: A way for the database to handle a new location with differing menu items. 

2: A ManyToMany relationship on the menu items to an ingredients table and get those items to populate in the API

3: A way to handle exceptions with error messaging on front end and/or back end.

4: A custom field(s) to the API that improves the functionality of the restaurant front end


COULD:

1: Override the save, pre_save, or post_save methods in your models use a free API to grab an image that saves as a url in your database.

2: A class based views or decorators in Django to protect routes.

3: A Generated csv export of the data in the database with a new route containing all the required information.

4: User groups to assign the restaurant owners a subset of abilities when they login to update data in the Django Administration. Enable the registration page for Django Admin.


WONT: 

1: Some funky bass riffs