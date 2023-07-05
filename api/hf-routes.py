from flask import request, jsonify
from hf-wrapper import ModelManager

manager = ModelManager('./')  

def download_model():
    model_name = request.json.get('model_name')
    model_path = manager.download_model(model_name)

    return jsonify({'message': 'Model downloaded successfully', 'model_path': model_path})

def load_model():
    model_name = request.json.get('model_name')
    weight_path = request.json.get('weight_path')

    if weight_path is None:
        model_path = manager.download_model(model_name)
    else:
        model_path = weight_path

    model = manager.load_model(model_path)

    return jsonify({'message': 'Model loaded successfully'})

def get_directories():
    directories = manager.get_directories()

    return jsonify({'directories': directories})
