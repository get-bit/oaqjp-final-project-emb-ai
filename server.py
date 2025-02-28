''' Executing this function initiates the application of EmotionDetection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector") #Initiate the flask app

@app.route("/emotionDetector")
def emot_analyzer():
    '''This function retrieves the emotion scores from the emotion_detection module'''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Error: No text provided"

    # Call the emotion detection function
    result = emotion_detector(text_to_analyze)

    # Check if dominant_emotion is None
    if result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    # Format the response as defined
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
