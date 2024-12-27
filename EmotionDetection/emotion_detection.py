import json
import requests

def emotion_detect(text_to_analyse):
    """Model for emotion detection"""
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    myobj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=myobj, headers=header)

    formatted_response = json.loads(response.text)
    
    emotions = {}

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key=lambda e: emotions[e])

        emotions['dominant_emotion'] = dominant_emotion

    elif response.status_code == 400:
        emotions = {key: None for key, value in emotions}
        emotions['dominant_emotion'] = None
    
    return emotions
    