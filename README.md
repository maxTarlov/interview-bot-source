# Interview Bot Source Code

This open source repository serves as a companion to my interview bot, which answers arbitrary interview questions by selecting the most relevant response from a set of pre-written answers. While I have _not_ freely licensed the [demo site](https://maxtarlov.github.io/interview-bot-website/) and [accompanying notebooks](https://maxtarlov.github.io/interview-bot-website/how), anything you find in _this_ repository is free to use, subject to the MIT License. You can read more about my reasoning for this [here](https://maxtarlov.github.io/interview-bot-website/copyright).

## Getting started

If you have just downloaded this repository on your desktop or laptop, use the bash shell to run `source setup.sh`. This will create and activate a python virtual environment and install the necessary dependencies for you to run and test the code on your machine.

## Structure of this repository

There are three main directories in this repository: `cloud_function`, which is the back-end for the interview bot demo site `data`, which is the data used to create the interview bot, and `notebooks`, which contains versions of my notebooks that contain only the open source code.

### The `cloud_function` directory

As the name suggests, this directory is meant to be deployed as a serverless cloud function. Once deployed to the cloud, the software in this directory will accept users' questions and respond with appropriate answers. `matcher.py` contains the code for matching users' questions to pre-written answers, while `main.py` provides the main http interface.

### The `data` directory

This directory contains three files. `questions.tsv` enumerates each interview questions I used for training and the webpage I scraped it from. `sources.tsv` lists 99 webpages and whether their contents have already been scraped and added to `questions.tsv`. `answers.json` maps example interview questions to pre-written answers. `cloud_function/matcher.py` finds which question in `answers.json` is most similar to a user-submitted question and returns the answer corresponding to the most similar example question.

## Roadmap

- [x] Write `setup.sh`
- [x] Copy over data repository
- [ ] Make demo version of cloud-function
- [ ] Write `deploy_cloud_function.sh`
- [ ] Finalize notebook
- [ ] Bring notebook into open source repo