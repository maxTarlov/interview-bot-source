#!/bin/bash

# Run this function to deploy the cloud-function to GCP

INTERVIEW_BOT_SOURCE_LINK=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )/..
cd $INTERVIEW_BOT_SOURCE_LINK

# make sure cloud function data is up-to-date
utils/refresh_cloud_function_data.sh

gcloud functions deploy handle-question\
  --gen2\
  --runtime python39\
  --region=us-west1\
  --source=cloud-function\
  --entry-point route_requests\
  --trigger-http\
  --allow-unauthenticated\
  --memory=1024MB\
  --max-instances=3
