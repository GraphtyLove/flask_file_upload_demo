from flask import Flask, request
from flask_cors import CORS
import cv2
from uuid import uuid4
import os


# Create the API object
app = Flask(__name__)
# Open CORS to avoid integration issues
CORS(app)


# Route to verify that the API is running
@app.route('/', methods=['GET'])
def home():
    return "Alive"


@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from post request
    image = request.files["image"]
    
    # Create a unique filename to avoid overwriting
    uuid = str(uuid4())
    
    # Define the image name with the UUID
    image_name = f"{uuid}_{image.filename}"
    
    # Define the image path where the image will be saved
    image_path = f"/tmp/{image_name}"
    
    # Save the image
    image.save(image_path)

    # Make your prediction (insert your code here)
    # response = prediction(image_path)
    
    # Read the image to verify that the image is readable (Optional)
    opencv_image = cv2.imread(image_path)
    print("Image shape: ", opencv_image.shape)

    # Delete the image to save space
    os.remove(image_path)

    # Return the response (adapt it with your prediction)
    return {
        "prediction": 1,
    }


if __name__ == "__main__":
    # ------ LOCAL DEVELOPMENT ------
    # Run the API locally on port 5000
    app.run(host='127.0.0.1', port=5000, debug=True)
    
    # ------ Docker version ------
    # PORT = os.environ.get('PORT', 5000)
    # app.run(host='0.0.0.0', port=PORT)