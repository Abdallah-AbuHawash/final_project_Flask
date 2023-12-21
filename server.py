"""
This module sets up a Flask server for an Emotion Detection application.
It provides routes to render the web interface and to process emotion detection requests.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index HTML page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():
    """
    Handle GET request to detect emotion from the given text.
    Extracts text from query parameters and returns the emotion analysis.
    """
    text = request.args.get('textToAnalyze')

    result = emotion_detector(text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy':{result['joy']}, "
                "and 'sadness': {result['sadness']}. The dominant emotion is "
                f"{result['dominant_emotion']}.")
    return response

if __name__ == '__main__':
    app.run(debug=True)
