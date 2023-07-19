# Flask-MongoDB REST API

Now fork and clone this repository, and then run the command - `pip install -r requirements.txt` and `python3 app.py`
This will start your Flask app that runs on - `http://127.0.0.1:5000`

Now you can use any testing tool like Postman to hit the following endpoints and verify the results-
1. `GET /users` - To fetch all the user records.
2. `GET /users/<id>` - To fetch the user with an individual-provided ID.
3. `POST /users` - JSON data of the new user is required to create a new user.
4. `PUT /users/<id>` - To update the information of any existing user.
5. `DELETE /user/<id>` - Delete the data of any user respective to the provided user ID.
