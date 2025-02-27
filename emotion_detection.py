import json
import requests

def emotion_detector(text_to_analyze):
    '''This function uses the Watson NLP libraries to return emotion reading'''
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the payload with the text to the be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=headers)

    # Return the text
    return {response.text}