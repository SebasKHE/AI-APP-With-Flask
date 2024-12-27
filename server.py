"""This module runs the Flask Web App to interact with the 
    Emotion Detection model"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detect

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Get the request and give a response in Web app server"""
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detect(text_to_analyse)

    if response['dominant_emotion'] is not None:
        emotions = dict(list(response.items())[:-1])

        emotions_str = ', '.join(f"'{key}': {value}" for key, value in emotions.items())

        dominant_emotion = response['dominant_emotion']

        return f"""For the given statement, the system response
                is {emotions_str}. The dominant emotion is {dominant_emotion}."""

    return "Invalid text! Please try again"

@app.route("/")
def render_index_page():
    """Render the index page with the template"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
