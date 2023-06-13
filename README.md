# What's for Dinner

## Live Link: https://whats-for-dinner.herokuapp.com
- Frontend Repo: https://github.com/marotella/whats-for-dinner-frontend
- Backend Deployed: https://whats-for-dinner-backend.herokuapp.com

What's For Dinner, is an application which allows a user to track what ingredients they have in thier kitchen, and find recipes that they can make using those ingredients. The application works to reduce food waste, ease deicsion making around meal times, and discover new recipes.

## Technologies Used

- Flask
- SQLite/Postgresql
- React
- Tailwind
- Flexbox
- Heroku 
The application also uses data from an external API: https://www.themealdb.com/api.php


## Installation:
- Necessary to install: Flask, React, Tailwind, Heroku, Peewee, SQLite, CORS, Dotenv, Gunicorn

## MVP Goals

- A full CRUD app for ingredients.
- User authorization in place for update, create, and delete.
- The ability to search an API for recipes with selected ingredients.
- The ability to register, login, and logout from an account.

## Stretch Goals

- One-to-many for a user's ingredients, and/or saving recipes.
- Implementing Tailwind for CSS. - Completed



## Approach
- Developed full CRUD operations using Flask and tested routes with Postman.
- Fetched data from external API and reviewed data structure using Postman
- Developed frontend components and connected to the backend.
- Implemented user authorization, by using state in React.
- Included a third party API - https://www.themealdb.com/api.php for search and data images
- Deployed online and accessible to the public via Heroku
- Used Trello throughout the process for project management.

## Models

Ingredients:
 - ingredient: String
 - quantity: integer

Users:
 - username: String
 - email: email
 - password: String

## Routes

User Routes:
- Register: users/register - POST
- Login: users/login - POST
- Logout: users/logout - GET

Ingredient Routes:
- Index: /ingredients - GET
- Show: /ingredients/<id> - GET
- Update: /ingredients/<id> - PUT
- Create: /ingredients - POST
- Delete: /ingredients/<id> - DELETE

Recipe Routes:
- Search: /ingredients/api/search - POST
- Show: /ingredients/api/recipes/<recipe_id> - GET

## User Stories

This application was designed for folks who enjoy cooking, want to reduce food waste, but may not have time or energy to find new recipes. 
- The user to can mantain a database of their kitchen ingredients. The can view, edit, and update items in their kitchen. 
- They can then use the ingredients they have to search a database of recipes that use those ingredients. 
- They can view the full recipe and instructions on how to make the dish as well. 
- Users have to create an account, and login to access these features.


## Initial Wireframe

Home: 

## Register/Sign in:
![image-1](https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/c1015046-6988-4b61-b158-b9c043a86a93)

## New form:
![image](https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/19243f11-0961-4b63-a5a1-1d256806f535)

## Show:
<img width="540" alt="Screenshot 2023-06-12 at 7 51 22 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/a216454b-50e3-4f50-84fa-874ec5203ebd">

## Index:
<img width="460" alt="Screenshot 2023-06-12 at 7 51 44 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/83170ae5-a4b1-4eb9-91e6-444088889fd9">

## Edit:
<img width="460" alt="Screenshot 2023-06-12 at 7 52 03 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/22d4011d-05e2-4340-9b27-e8ab43999f51">

## Search:
<img width="460" alt="Screenshot 2023-06-12 at 7 51 51 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/c5d3cdff-d969-436e-a561-0c6baf6db9c8">

## Search result:
<img width="460" alt="Screenshot 2023-06-12 at 7 52 13 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/8bf347c9-1735-430b-8d4c-e384c9b7e521">

 
## Final Design
 ## Home: 
<img width="1318" alt="Screenshot 2023-06-12 at 7 55 04 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/5a3b42de-1eb5-4446-8ba0-08c8cbd5d014">
 
## Register/Sign in:
<img width="1318" alt="Screenshot 2023-06-12 at 7 55 16 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/fbfb5675-4a9d-4ba0-9e49-0c53629c1197">
<img width="1318" alt="Screenshot 2023-06-12 at 7 55 32 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/74d3ae20-954c-4d27-a681-09ef23b723f1">


## New form:
<img width="1318" alt="Screenshot 2023-06-12 at 7 56 30 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/d6350eea-7fe7-4256-aac3-b4e004e2040c">

 
## Show:
<img width="1318" alt="Screenshot 2023-06-12 at 7 56 13 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/8d8ead02-68a5-46b4-8ae0-e4d34d146d7e">

 
## Index:
<img width="1318" alt="Screenshot 2023-06-12 at 7 55 59 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/bb0a11c6-f29f-4729-85e9-4f9b3d7ceb0a">

## Edit:
<img width="1318" alt="Screenshot 2023-06-12 at 7 56 22 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/cb0b0207-5aac-4460-abbd-f92413b068b9">

 
## Search:
<img width="1288" alt="Screenshot 2023-06-12 at 7 57 11 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/188e8493-b61e-48e6-a451-9e6fc36c036b">

 
## Search result:
<img width="1288" alt="Screenshot 2023-06-12 at 7 57 37 PM" src="https://github.com/marotella/whats-for-dinner-frontend/assets/111547566/16a41445-2757-41b6-bce0-d133cdeb0fcd">


## Next Steps:

- Continue to modify the code for mobile rendering.
- Implement a one to many relationship to allow for multiple users.
- Add in a shopping list feature 
