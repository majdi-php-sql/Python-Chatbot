from transformers import pipeline  # I imported the pipeline function from transformers to use pre-trained models

def get_nlp_model():
    """
    I wrote this function to load a pre-trained question-answering model for natural language processing.
    """
    nlp_model = pipeline("question-answering")  # I initialized the model for question-answering tasks
    return nlp_model  # I returned the model for use in processing user questions
