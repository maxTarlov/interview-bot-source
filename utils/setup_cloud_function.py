"""Download and cache language model and precompute encodings for golden questions  """

import os
from sentence_transformers import SentenceTransformer
import json
import pickle

REPO_ROOT_DIR = os.path.dirname(os.path.dirname(__file__))
CLOUD_FUNCTION_DATA_DIR = os.path.join(REPO_ROOT_DIR, 'cloud_function', 'data')


def main():
    print('Downloading and caching lanuage model...')
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'config.json'), 'r') as config_file:
        config = json.load(config_file)
    assert config['using sentence_transformers']  # this code assumes you are using sentence_transformers
    model = SentenceTransformer(config['model name'], cache_folder=CLOUD_FUNCTION_DATA_DIR)
    model_folder = '_'.join(['sentence-transformers', config['model name']])
    assert os.path.isdir(os.path.join(CLOUD_FUNCTION_DATA_DIR, model_folder))
    config['model folder'] = model_folder
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'config.json'), 'w') as config_file:
        json.dump(config, config_file)


    print('Precomputing encodings for golden questions...')
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'answers.json'), 'r') as answers_file:
        golden_questions = list(json.load(answers_file).keys())
    golden_questions.remove('[fallback]')
    golden_question_encodings = model.encode(golden_questions)
    with open(os.path.join(CLOUD_FUNCTION_DATA_DIR, 'golden_question_encodings.pickle'), 'wb') as encodings_file:
        pickle.dump(golden_question_encodings, encodings_file)

if __name__ == '__main__':
    main()