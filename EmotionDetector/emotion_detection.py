"""
emotion_detection.py
Detects emotion from a given text input using IBM Watson NLP API.
"""

import requests
import json


def emotion_detector(text_to_analyze):
    """
    Analyzes the given text and returns a dictionary of emotion scores and the dominant emotion.
    Returns None values with status_code 400 for blank input.
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'joy': None,
            'sadness': None,
            'fear': None,
            'anger': None,
            'disgust': None,
            'dominant_emotion': None,
            'status_code': 400
        }

    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    joy_score = emotions["joy"]
    sadness_score = emotions["sadness"]
    fear_score = emotions["fear"]
    anger_score = emotions["anger"]
    disgust_score = emotions["disgust"]

    emotion_scores = {
        'joy': joy_score,
        'sadness': sadness_score,
        'fear': fear_score,
        'anger': anger_score,
        'disgust': disgust_score
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    return {
        'joy': joy_score,
        'sadness': sadness_score,
        'fear': fear_score,
        'anger': anger_score,
        'disgust': disgust_score,
        'dominant_emotion': dominant_emotion,
        'status_code': 200
    }
