import requests

"""
calls diagnostic MS to check distribution of users in interventiongroup
"""
def sendReport(username):
    url = "https://ortho-diagnostics-prod.herokuapp.com/api/schueler"    
    headers = {'Username': username, 'Authorization': 'Bearer C0ba50f075d02a520732dc07ea6c6f3f527bd832'}
    result = requests.get(url, headers=headers)
    print(result.status_code)