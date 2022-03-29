#! /usr/bin/python
# Imports
import requests

def send_simple_message():
    print("I am sending an email.")
    return requests.post(
        "https://api.mailgun.net/v3/sandbox73d63b987ac34fbfb79462fc3985ff2b.mailgun.org/messages",
        auth=("api", "34eb531537e3e4d0f7defdbe3aadafc3-62916a6c-e9942af1"),
        data={"from": 'hello@example.com',
            "subject": "Visitor Alert",
            "html": "<html> Your Raspberry Pi recognizes someone. </html>"})
                      
request = send_simple_message()
print ('Status: '+format(request.status_code))
print ('Body:'+ format(request.text))
