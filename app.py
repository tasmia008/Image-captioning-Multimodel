# app.py
from flask import Flask, request, jsonify
from caption_model.py import generate_caption

app = Flask(__name__)

@app.route('/caption', methods=['POST'])
def caption():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image = request.files['image']
    image_path = f'./uploads/{image.filename}'
    image.save(image_path)

    caption = generate_caption(image_path)
    return jsonify({'caption': caption})

if __name__ == '__main__':
    app.run(debug=True)
