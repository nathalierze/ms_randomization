import requests

"""
calls diagnostic MS to check distribution of users in interventiongroup
"""
def sendReport():
    url = "http://host.docker.internal:8002/api/schueler"    
    result = requests.get(url)
    print(result.status_code)