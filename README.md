# Interview Bot Source Code

This open source repository serves as a companion to my interview bot, which answers arbitrary interview questions by selecting the most relevant response from a set of pre-written answers. While I have _not_ freely licensed the [demo site](https://maxtarlov.github.io/interview-bot-website/) and [accompanying notebooks](https://maxtarlov.github.io/interview-bot-website/how), anything you find in _this_ repository is free to use, subject to the MIT License. You can read more about my reasoning for this [here](https://maxtarlov.github.io/interview-bot-website/copyright).

## Getting started

If you have just downloaded this repository on your desktop or laptop, use the bash shell to run `source setup.sh`. This will create and activate a python virtual environment and install the necessary dependencies for you to run and test the code on your machine. Whenever you update a file in the `data` directory (to use a different language model or change the chatbot's answers, for example) you will need to run `utils/refresh_cloud_function_data.sh`. This script will be run once by `setup.sh`.

Once you have run setup.sh, start up the development server by running `functions-framework --debug --target="route_requests"` and make a GET request in your browser by going to http://localhost:8080 for the default response, or http://localhost:8080?q=what+is+your+dream+job to get the answer to the question "what is your dream job?" 


If you wish to deploy the chatbot as a Google Cloud Function, you can follow [this tutorial](https://cloud.google.com/functions/docs/create-deploy-gcloud-1st-gen).

## Structure of this repository

There are three main directories in this repository: `cloud_function`, which is the back-end for the interview bot demo site `data`, which is the data used to create the interview bot, and `notebooks`, which contains versions of my notebooks that contain only the open source code. There is also a `utils` directory which contains some useful scripts.

### The `cloud_function` directory

As the name suggests, this directory is meant to be deployed as a serverless cloud function. Once deployed to the cloud, the software in this directory will accept users' questions and respond with appropriate answers. `matcher.py` contains the code for matching users' questions to pre-written answers, while `main.py` provides the main http interface. The `cloud_function/data` contains the data needed in production for the cloud function to work and is copied over from the main `data` directory.

### The `data` directory

In this directory, `questions.tsv` contains the entire corpus of interview questions I used for creating the chatbot, while `answers.jon` contains a smaller mapping of "golden" interview questions to pre-written answers. The answers are coppied to `cloud_function/data`. From there, `cloud_function/matcher.py` finds which question in `answers.json` is most similar to a user-submitted question and returns the answer corresponding to the most similar example question.

## Roadmap

- [x] Write `setup.sh`
- [x] Copy over data repository
- [x] Make demo version of cloud-function
- [ ] Finalize notebook
- [ ] Bring notebook into open source repo