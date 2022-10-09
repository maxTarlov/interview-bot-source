import logging

LOGGING_LEVEL = 'INFO'
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_LEVEL)

import os
import pickle
import json

from sentence_transformers import SentenceTransformer
from sentence_transformers.util import cos_sim

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

with open(os.path.join(DATA_DIR, 'config.json'), 'r') as config_file:
    config = json.load(config_file)

model = SentenceTransformer(os.path.join(DATA_DIR, config['model folder']))

with open(os.path.join(DATA_DIR, 'golden_question_encodings.pickle'), 'rb') as encodings_file:
  golden_question_encodings = pickle.load(encodings_file)

with open(os.path.join(DATA_DIR, 'answers.json'), 'r') as answers_file:
  question_answer_mappings = json.load(answers_file)  # a dict, {<question>: <answer>}

fallback_answer = question_answer_mappings.pop('[fallback]')
answers = tuple(question_answer_mappings.values())
golden_questions = tuple(question_answer_mappings.keys())

from typing import TYPE_CHECKING, Callable, Tuple

if TYPE_CHECKING:
  # we only need to import torch if we are using a static type checker like mypy
  from torch import Tensor

def score_similarities(question: str, encoder: Callable=model.encode, 
    golden_question_embeddings: 'Tensor'=golden_question_encodings) -> 'Tensor':
  """
  Return a vector of similarity scores between the embedding of question and 
  the embeddings for the golden questions using cosine similarity.
  """
  question_embedding = encoder(question)
  # If the encodings don't have the same dimentionality something has gone wrong
  assert question_embedding.shape[0] == golden_question_embeddings.shape[1]
  return cos_sim((question_embedding), golden_question_embeddings)[0]

def get_best_match(question: str, answers: Tuple=answers, 
    fallback_answer: str=fallback_answer, threshold=0.55, 
    encoder: Callable=model.encode, 
    golden_question_embeddings: 'Tensor'=golden_question_encodings) -> str:
  """
  Determine the best pre-written answer to the question.
  """
  similarity_scores = score_similarities(question, encoder, 
    golden_question_embeddings)
  best_match_index = int(similarity_scores.argmax())
  confidence = float(similarity_scores[best_match_index])
  assert confidence == max(similarity_scores)
  logger.info('Confidence: '+str(confidence))

  assert len(golden_questions) == len(answers)
  result: str

  if confidence > threshold:
    logger.info('Matched question: '+golden_questions[best_match_index])
    result = answers[best_match_index]
  else:
    logger.info('confidence < threshold, using fallback')
    logger.debug('Next best question: '+golden_questions[best_match_index])
    logger.debug('Next best answer: '+answers[best_match_index])
    result = fallback_answer
  return result

if __name__ == '__main__':
  print(get_best_match('Tell me about yourself'))
