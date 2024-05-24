# Use an official node image as a parent image
FROM node:20.13-alpine3.19

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the app
RUN npm run build

# Set environment variable for the port
ENV PORT=8080

# Expose the port the app runs on
EXPOSE 8080

# Start the app
CMD ["npm", "start"]