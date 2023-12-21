import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not text_to_analyze.strip():  # Checks for None or blank input
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()

    # Extracting emotion scores
    emotions = response_data['emotionPredictions'][0]['emotion']

    # Finding the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Preparing the final output
    output = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return output
