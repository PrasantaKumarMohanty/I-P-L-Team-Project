# I-P-L-Team-Project
This "I P L Team Project" is developed by Prasanta Kumar Mohanty using Python with Django web framework, HTML &amp; CSS.

## Screenshots

1. HOME Page -

![Screenshot (300)](https://user-images.githubusercontent.com/92419941/146123679-15cf7837-063d-43a6-ab5d-a4989d5dc559.png)

2. Add a new team page -

![Screenshot (292)](https://user-images.githubusercontent.com/92419941/146123939-ce75b72b-087b-4c8e-9341-7a0e666b27db.png)

3. Add a new player page -

![Screenshot (293)](https://user-images.githubusercontent.com/92419941/146124089-b3135c5c-0752-4ac6-8826-f8c389aa6e9c.png)

4. Search page -

![Screenshot (294)](https://user-images.githubusercontent.com/92419941/146124150-9329f94d-16d2-499c-afc1-9478d7df53de.png)

5. Team Details page -
![Screenshot (295)](https://user-images.githubusercontent.com/92419941/146124281-ccc894ff-90c1-4b6c-b11f-dcc3cc30f864.png)

6. Player list of selected team -
![Screenshot (296)](https://user-images.githubusercontent.com/92419941/146124452-ee14df4b-6dbf-4e2f-8be4-8770feff33bf.png)

7. Player profile page -
![Screenshot (297)](https://user-images.githubusercontent.com/92419941/146124646-6bbb3758-4c9a-46e5-9c37-171c6dfdaf6d.png)

8. Team edit page -
![Screenshot (298)](https://user-images.githubusercontent.com/92419941/146124850-1a78b52b-76ae-45fc-9c39-ad2a488bff79.png)

9. Footer -
![Screenshot (299)](https://user-images.githubusercontent.com/92419941/146125532-121c205f-9fb5-459c-895e-bdfee673b40a.png)

## Technologies

* Python - 3.7.9
* Django - 3.2.10
* HTML
* CSS
* SQLite
## Setup

1. Install Python and Pipenv -
* Python

* virtualenv
2. Create a project folder -
  ```
      $ mkdir project
      $ cd project
  ```
   
3. Create a python virtualenv, and activate the environment to install requirements.
   ```
      $ virtualenv env
      $ source env/Script/activate
    ```
4. Install project Dependencies -
    ```
      $ pip install -r requirements.txt
    ```
5. Set the Database(Make sure you are in directory same as manage.py)
    ```
      $ python manage.py makemigrations
      $ python manage.py migrate
    ```
6. Create SuperUser -
    ```
      $ python manage.py createsuperuser
    ```
7. Run the server -
    ```
      $ python manage.py runserver
    ```
## Status
Project is: Done
