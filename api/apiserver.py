from flask import Flask
from hf-routes import download_model, load_model

app = Flask(__name__)

# Register the routes
app.add_url_rule('/download', view_func=download_model, methods=['POST'])
app.add_url_rule('/load', view_func=load_model, methods=['POST'])

if __name__ == '__main__':
    app.run()
