import requests
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()
"""
calls diagnostic MS to check distribution of users in interventiongroup
"""


def sendReport(username):
    url = "https://ortho-diagnostics-prod.herokuapp.com/api/schueler"
    headers = {
        "Username": username,
        "Authorization": env('BEARER_KEY'),
    }
    result = requests.get(url, headers=headers)
    print(result.status_code)
