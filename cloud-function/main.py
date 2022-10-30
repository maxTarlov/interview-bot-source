import matcher
import functions_framework

import logging

logger = logging.getLogger(__name__)

ALLOW_METHODS = 'GET'

DEFAULT_QUESTION = 'Tell me about yourself.'
DEFAULT_ANSWER = matcher.question_answer_mappings[DEFAULT_QUESTION]

def handle_get(request):
    """
    GET requests are to ask the bot an interview question. If there is an argument "q"
    in the url, use the matcher.get_best_match function to serve the best response. If
    there is no argument "q" in the url, return the default answer. All GET requests
    are logged in GCP Firestore and the unique key for that log is returned along with
    the user's question and the answer to that question.
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json'
    }

    if 'q' in request.args and request.args['q'] != '':
        question = request.args['q']
        answer = matcher.get_best_match(question)
        body = {
            'user-question': question,
            'bot-answer': answer
        }
    else:
        log_id = 42
        body = {
            'user-question': DEFAULT_QUESTION,
            'bot-answer': DEFAULT_ANSWER
        }
    return body, 200, headers

@functions_framework.http
def route_requests(request):
    # For more information about CORS and CORS preflight requests, see:
    # https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request

    # Set CORS headers for the preflight request
    if request.method == 'OPTIONS':
        headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': ALLOW_METHODS,
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '86400'
        }
        return ('', 204, headers)
    else:
        return handle_get(request)
