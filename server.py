"""
server.py
Flask app that serves a basic web UI and handles emotion detection requests.
"""

from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Renders the homepage (index.html)."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emot_detector():
    """
    Receives a GET request with 'textToAnalyze' query param.
    Returns emotion detection response or an error message for invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    if response["status_code"] == 400 or response["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    return (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
    f"'fear': {response['fear']}, 'joy': {response['joy']}, "
    f"'sadness': {response['sadness']}, 'dominant_emotion': {response['dominant_emotion']}"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
