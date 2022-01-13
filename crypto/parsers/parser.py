import requests

def get_data_from_url(url):
    headers = {
        "accept": "appication/json",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    return req.text