# Flask App and CouchDB with Docker

This project sets up a Flask application and CouchDB as services using Docker and Docker Compose. Follow the steps below to build, start, and manage the containers.

## Steps to Build, Start, and Manage Containers:

### 1. Build the Containers

Run the following command to build the containers as defined in your `docker-compose.yml` file:

docker-compose build

2. Start the Containers
Once the containers are built, start them with:
docker-compose up

3. Access the Application
The Flask application will be available at: http://localhost:5000
CouchDB will be available at: http://localhost:5984

4. Stop the Containers
To stop the running containers, use:
docker-compose down

5. View Logs in Real-Time
To monitor the logs of your containers, run the following command:
docker-compose logs -f

6. Run in Detached Mode (Background)
If you want to run the containers in detached mode (in the background), use:
docker-compose up -d
_______________________________________________________________________________

or to just use in local ,
to start :
>> python app.py