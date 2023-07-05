import argparse
import requests

def download_model(model_name, api_url):
    payload = {
        'model_name': model_name
    }
    response = requests.post(f'{api_url}/download', json=payload)
    if response.status_code == 200:
        data = response.json()
        model_path = data['model_path']
        print(f"Model downloaded successfully and saved at {model_path}")
    else:
        print("Failed to download the model")

def load_model(model_name, weight_path, api_url):
    payload = {
        'model_name': model_name,
        'weight_path': weight_path
    }
    response = requests.post(f'{api_url}/load', json=payload)
    if response.status_code == 200:
        print("Model loaded successfully")
    else:
        print("Failed to load the model")

def get_directories(api_url):
    response = requests.get(f'{api_url}/directories')
    if response.status_code == 200:
        data = response.json()
        directories = data['directories']
        for directory, files in directories.items():
            print(f"{directory}:")
            for file in files:
                print(f"  {file}")
    else:
        print("Failed to retrieve directories")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API Client')
    parser.add_argument('--api_url', required=True, help='API URL')
    parser.add_argument('--command', required=True, choices=['download', 'load', 'directories'], help='Command')
    parser.add_argument('--model_name', help='Model name')
    parser.add_argument('--weight_path', help='Weight path (optional)')

    args = parser.parse_args()

    if args.command == 'download':
        download_model(args.model_name, args.api_url)
    elif args.command == 'load':
        load_model(args.model_name, args.weight_path, args.api_url)
    elif args.command == 'directories':
        get_directories(args.api_url)
