import json
import requests

def emotion_detector(text_to_analyze):
    '''This function uses the Watson NLP libraries to return emotion reading'''
    # Initiate emotion scores
    anger_score = None
    disgust_score = None
    fear_score = None
    joy_score = None
    sadness_score = None
    dominant_emotion = None

    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create the payload with the text to the be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=input_json, headers=headers)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    emotions_response = formatted_response['emotionPredictions'][0]
    emotion_dict = emotions_response['emotion']
    anger_score = emotion_dict['anger']
    disgust_score = emotion_dict['disgust']
    fear_score = emotion_dict['fear']
    joy_score = emotion_dict['joy']
    sadness_score = emotion_dict['sadness']
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)
    new_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
        }

    # Return the parsed response
    return new_dict