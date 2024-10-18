import json
import requests



def get_token():
    token_url = 'https://cofaserve-api.coface.com/authentication/v1/token'
    bearer_token = 'X5IVIRVle82rsLH52KHXf3d2jkKKa03SAxuFyFX9'
    username = 'CG440520'
    password = 'Admiç!9876'
    policy = '453994155'

    headers = {
        'x-api-key': bearer_token,
        'content-type': 'application/json',
        'x-cof-policy-number': policy
    }

    payload = {'username': username, 'password': password, 'grant_type': 'password'}

    response = requests.post(token_url, headers=headers, data=json.dumps(payload))

    print(response.text)


if __name__ == "__main__":
    get_token()