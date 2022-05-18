import requests

"""
calls diagnostic MS to check distribution of users in interventiongroup
"""
def sendReport():
    url = "https://ortho-diagnostics-prod.herokuapp.com/api/schueler"    
    result = requests.get(url)
    print(result.status_code)