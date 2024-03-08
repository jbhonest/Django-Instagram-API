# Django Instagram API
## Project Overview
This Django app is designed to replicate the basic functionality of Instagram, providing features such as posting photos, sharing stories, liking posts, commenting, following other users, sending direct messages, and tracking post and profile views. It utilizes the Django Rest Framework (DRF) to handle API endpoints for seamless communication between the frontend and backend.

## Features

**1. User Authentication**
   - Users can register an account.
   - Users can log in and log out securely.

**2. Posts and Stories**
   - Users can create and share posts.
    - Support for uploading and displaying images.
   - Stories feature with a limited duration.
  
**3. Interactions**
   - Like posts to show appreciation.
   - Comment on posts to engage with other users.
  
**4. Social Connections**
  - Follow other users to stay updated on their activities.
  - View a feed of posts from followed users.
  
**5. Direct Messaging**
  - Send and receive direct messages privately.

**5. Analytics**
- Track post views to understand content popularity.
- Monitor profile views for user engagement insights.


## Installation
1. Clone the repository:
```bash
git clone https://github.com/jbhonest/django-instagram-api.git
```

2. Navigate to the project directory:

```bash
cd django-instagram-api
```

3. In **instagram** folder rename sample_settings.py to local_settings.py

4. Generate a SECRET_KEY and save it in local_settings.py

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Apply migrations to set up the database:
```bash
python manage.py migrate
```

7. Run the development server:
```bash
python manage.py runserver
```


## API Endpoints
* Content API root: http://127.0.0.1:8000/content/
* User activity API root: http://127.0.0.1:8000/user_activity/
* User panel API root: http://127.0.0.1:8000/user_panel/
* Analytics API root: http://127.0.0.1:8000/logger/

* Messaging API root: http://127.0.0.1:8000/direct/

* To register, send a post request to: http://127.0.0.1:8000/user_panel/register/

* To login, send a post request to: http://127.0.0.1:8000/user_panel/login/

Use tools like curl, httpie, or Postman to interact with the API.



## Django Admin
First, create an admin user:
```bash
python manage.py createsuperuser
```
Then, access the Django admin interface at http://127.0.0.1:8000/admin/ to manage contacts.


---
Developed by Jamal Badiee (jbhonest@yahoo.com)