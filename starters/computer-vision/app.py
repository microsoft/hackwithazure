# app.py
import os, base64, json, requests
from flask import Flask, render_template, request

# Load system variables with dotenv
from dotenv import load_dotenv
load_dotenv()

# Load keys
endpoint = os.environ["COGSVCS_CLIENTURL"]
key = os.environ["COGSVCS_KEY"]

# Create vision_client
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException

vision_credentials = CognitiveServicesCredentials(key)
vision_client = ComputerVisionClient(endpoint, vision_credentials)

# Create the application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # If it"s a GET, just return the form
    if request.method == "GET":
        # Display default page
        return render_template("index.html", image_uri="/static/placeholder.png")

    # Read the file from the form
    image = request.files["file"]

    # Retrieve text from picture
    messages = extract_text_from_image(image, vision_client)

    # Reset stream back to the beginning
    image.seek(0)

    # Create a uri to display image on form
    image_uri = "data:;base64," + base64.b64encode(image.read()).decode("utf-8")

    # Display result
    return render_template("index.html", image_uri=image_uri, messages=messages)

def extract_text_from_image(image, client):
    result = client.recognize_printed_text_in_stream(image=image)

    lines=[]
    if len(result.regions) == 0:
        lines.append("Photo contains no text")
    else:
        for region in result.regions:
            for line in result.regions[0].lines:
                text = " ".join([word.text for word in line.words])
                lines.append(text)
    return lines
