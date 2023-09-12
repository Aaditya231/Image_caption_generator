import os
from flask import Flask, render_template, request, jsonify
from main import generate_caption_for_image  # Import your caption generation function

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_caption():
    # Check if 'image' field is in the POST request
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['image']

    # Check if a file was selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the uploaded image to a temporary location
    image_path = 'temp_image.jpg'
    file.save(image_path)

    # Generate caption for the uploaded image using your function from main.py
    caption = generate_caption_for_image(image_path)

    # Clean the caption
    caption = caption.replace("startseq", "").replace("endseq", "")

    return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(debug=True)
