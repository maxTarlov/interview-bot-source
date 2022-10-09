"""Download and cache language model and precompute encodings for golden questions  """

import os
from sentence_transformers import SentenceTransformer
import json
import pickle

REPO_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
CLOUD_FUNCTION_DATA_DIR = os.path.join(REPO_ROOT_DIR, 'cloud_function', 'data')

MODEL_NAME = 'all-MiniLM-L6-v2'

def main():
    print('Downloading and caching lanuage model...')
    model = SentenceTransformer(MODEL_NAME, cache_folder=os.path.join(CLOUD_FUNCTION_DATA_DIR, 'encoder'))

    print('Precomputing encodings for golden questions...')
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'answers.json'), 'r') as answers_file:
        golden_questions = list(json.load(answers_file).keys())
    golden_questions.remove('[fallback]')
    golden_question_encodings = model.encode(golden_questions)
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'golden_question_encodings.pickle'), 'wb') as encodings_file:
        pickle.dump(golden_question_encodings, encodings_file)

if __name__ == '__main__':
    main()