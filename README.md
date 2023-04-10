# Ankorstore Support chat

This project consists of a Flask server and a React frontend app, both of which are containerized using Docker. Before running the project, make sure you have `.env` file configured. Please make a copy of `.env.example` locally (with the name `.env`) and configure your `OPENAI_API_KEY`.

To run the stack locally you can run the following command:

```
docker-compose build
docker-compose up
```
- The Flask API will be available on `127.0.0.1:5000`
- The Application will be available on `127.0.0.1:3000`

## Server

The server is built from the Python 3.9 base image and runs on port 5000. It sets the working directory to `/app` and copies the `requirements.txt` file into the container to install the necessary dependencies. Then, it copies the rest of the application files and sets the environment variable for the Flask app. Finally, it exposes port 5000 and starts the server using the `flask run` command.

To build and run the server, use the following commands:

```
docker build -t server .
docker run -p 5000:5000 server
```

## Frontend App

The frontend app is built from the Node.js 14-alpine base image and runs on port 3000. It sets the working directory to `/app` and copies the `package.json` and `package-lock.json` files into the container to install the necessary dependencies. Then, it copies the rest of the application files and builds the React app using the `npm run build` command. Finally, it exposes port 3000 and starts the app using the `npm start` command.

To build and run the frontend app, use the following commands:

```
docker build -t frontend .
docker run -p 3000:3000 frontend
```

Note that these commands assume that you are running them in the same directory as the respective Dockerfiles. If not, you will need to adjust the paths accordingly.

## Additional Notes

- Make sure that you have Docker installed on your machine before building and running the containers.
- If you need to make changes to the code, you can rebuild the container(s) using the `docker build` command and then run the container(s) using the `docker run` command again.

