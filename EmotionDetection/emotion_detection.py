import requests
import json
from flask import Response

def emotion_detector(text_to_analyse):
    if not text_to_analyse:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }

   
    if Response.status_code == 200:
        formatted_response = json.loads(response.text).get("emotionPredictions", [])
            
        if formatted_response:
            formatted_response = formatted_response[0]["emotion"]
            dominant_emotion = max(formatted_response, key=formatted_response.get)
                
            anger_score = formatted_response.get('anger', 0)
            disgust_score = formatted_response.get('disgust', 0)
            fear_score = formatted_response.get('fear', 0)
            joy_score = formatted_response.get('joy', 0)
            sadness_score = formatted_response.get('sadness', 0)
        else:
            anger_score = disgust_score = fear_score = joy_score = sadness_score = 0
            dominant_emotion = "unknown"
        
    elif Response.status_code == 400:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
        
    elif Response.status_code == 500:
        return {
            'anger': None, 
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
        }
        
    else:
        anger_score = disgust_score = fear_score = joy_score = sadness_score = None
        dominant_emotion = None

    return {
        'anger': anger_score, 
        'disgust': disgust_score, 
        'fear': fear_score, 
        'joy': joy_score, 
        'sadness': sadness_score, 
        'dominant_emotion': dominant_emotion
    }
