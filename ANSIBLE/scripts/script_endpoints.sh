#!/bin/bash

# Define an array of endpoints
endpoints=(
    "http://192.168.0.14:5000"
    "http://192.168.0.14:5000/data"
    "http://192.168.0.14:5000/trigger_script"
    # Add more endpoints as needed
)
# Loop through each endpoint and check its response
for endpoint in "${endpoints[@]}"
do
    #echo "Checking endpoint: $endpoint"
    response=$(curl -s -o /dev/null -w "%{http_code}" "$endpoint")

    if [ "$response" != "200" ]; then
        echo "-------------------------------------------------------------------------------------"
        echo "Endpoint $endpoint is unreachable or returned status code: $response"
    fi
done
