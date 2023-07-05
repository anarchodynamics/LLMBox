import os
import time
from transformers import AutoModel

class ModelManager:
    def __init__(self, model_dir):
        self.model_dir = model_dir

    def download_model(self, model_name):
        timestamp = str(int(time.time()))
        model_path = os.path.join(self.model_dir, model_name + '_' + timestamp)

        print(f"Downloading {model_name}...")
        model = AutoModel.from_pretrained(model_name)
        os.makedirs(model_path, exist_ok=True)
        model.save_pretrained(model_path)
        print(f"Model downloaded and saved at {model_path}")

        return model_path

    def get_directories(self):
        directories = [name for name in os.listdir(self.model_dir) if os.path.isdir(os.path.join(self.model_dir, name))]
        directory_contents = {}

        for directory in directories:
            files = os.listdir(os.path.join(self.model_dir, directory))
            directory_contents[directory] = files

        return directory_contents
