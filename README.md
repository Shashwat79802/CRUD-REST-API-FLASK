# Flask-MongoDB REST API

To run this application, you need [Docker](https://docs.docker.com/engine/install/) installed in your respective application and must be logged in to [Docker Hub](https://hub.docker.com/).

Now fork and clone this repository, and then run the commands - 
1. `docker build -t <docker-hub-username>/flask-container:1.0.0 .`
2. `docker run -p 5000:5000 <docker-hub-username>/flask-container:1.0.0`

This will start your Flask app that runs on - HTTP://172.17.0.2:5000

Now you can use any testing tool like Postman to hit the following endpoints and verify the results-
1. `GET /users` - To fetch all the user records.
2. `GET /users/<id>` - To fetch the user with an individual-provided ID.
3. `POST /users` - JSON data of the new user is required to create a new user.
4. `PUT /users/<id>` - To update the information of any existing user.
5. `DELETE /user/<id>` - Delete the data of any user respective to the provided user ID.
