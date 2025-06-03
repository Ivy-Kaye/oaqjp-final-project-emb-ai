import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Corrected line
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    
    emotion_scores = {
        'joy': joy_score,
        'sadness': sadness_score,
        'fear': fear_score,
        'anger': anger_score,
        'disgust': disgust_score
    }

    dominant_emotion = max(emotion_scores, key = emotion_scores.get)
    return {'joy': joy_score, 'sadness': sadness_score, 'fear': fear_score, 'anger': anger_score, 'disgust': disgust_score, 'dominant_emotion': dominant_emotion}