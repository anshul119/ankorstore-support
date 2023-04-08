# Set the base image
FROM node:14-alpine

# Set the working directory
WORKDIR /app

# Copy the package and lock files and install the dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the React app
RUN npm run build

# Expose the port that the React app will run on
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]