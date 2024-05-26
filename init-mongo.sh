#!/bin/bash
# Copy the JSON data into the container and import it into the MongoDB collection
echo "Running MongoDB initialization script..."

# Since this script is copied into the mongo service and it is automatically execute  when 
# doing docker compose the host will be "localhost" since we are inside the "mongo" container
mongoimport --host localhost --db news --collection articles --type csv --file /data/data.csv --headerline

echo "MongoDB initialization script completed."