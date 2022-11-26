import matcher
import functions_framework
import json
import os
from random import sample

from google.cloud import firestore
db = firestore.Client()
question_logs = db.collection('question-logs')
user_feedback = db.collection('user-feedback')

ALLOW_METHODS = 'OPTIONS, GET, POST'
ALLOW_ORIGIN = 'maxtarlov.github.io, interview.tarlov.dev'

DEFAULT_QUESTION = 'Tell me about yourself.'
DEFAULT_ANSWER = matcher.question_answer_mappings[DEFAULT_QUESTION]

with open(os.path.join(matcher.DATA_DIR, 'suggestions.json'), 'r') as suggestions:
    SUGGESTED_QUESTIONS = json.load(suggestions)

def handle_get(request):
    """
    GET requests are to ask the bot an interview question. If there is an argument "q"
    in the url, use the matcher.get_best_match function to serve the best response. If
    there is no argument "q" in the url, return the default answer. All GET requests
    are logged in GCP Firestore and the unique key for that log is returned along with
    the user's question and the answer to that question.
    """

    headers = {
        'Access-Control-Allow-Origin': ALLOW_ORIGIN,
        'Content-Type': 'application/json'
    }

    if 'q' in request.args and request.args['q'] != '':
        question = request.args['q']
        answer = matcher.get_best_match(question)
        body = {
            'user-question': question,
            'bot-answer': answer,
            'default': False,
            'timestamp': firestore.SERVER_TIMESTAMP
        }
    else:
        body = {
            'user-question': DEFAULT_QUESTION,
            'bot-answer': DEFAULT_ANSWER,
            'default': True,
            'timestamp': firestore.SERVER_TIMESTAMP
        }

    _, log_ref = question_logs.add(body)
    del(body['timestamp'])  # not JSON serializable
    body['id'] = log_ref.id  # send unique id for feedback
    body['suggestions'] = sample(SUGGESTED_QUESTIONS, 3)
    return body, 200, headers

def handle_post(request):
    """
    POST requests are to provide feedback on the bot's response to a previous question.
    Expect a firestore document ID which corresponds to the ID of the question log.
    """

    headers = {'Access-Control-Allow-Origin': ALLOW_ORIGIN}
    try:
        request_json = request.get_json()
    except Exception as inst:
        return inst.description, 400, headers
    if 'id' in request_json and 'good' in request_json:
        user_feedback.document(str(request_json['id']))\
            .set({'good': request_json['good']})
        return '', 204, headers
    else:
        return 'Expected keys "id" and "good" in JSON', 400, headers
        

@functions_framework.http
def route_requests(request):
    # For more information about CORS and CORS preflight requests, see:
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        headers = {
        'Access-Control-Allow-Origin': ALLOW_ORIGIN,
        'Access-Control-Allow-Methods': ALLOW_METHODS,
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '86400'
        }
        return ('', 204, headers)
    elif request.method == 'POST':
        return handle_post(request)
    else:
        return handle_get(request)
