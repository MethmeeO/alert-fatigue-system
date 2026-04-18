import requests

API_KEY = "YOUR_API_KEY_HERE"

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }

    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        score = data["data"]["abuseConfidenceScore"]

        return score

    except:
        return 0
    