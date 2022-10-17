# APIs with python
# install requests
# pip install requests

import requests
# get
request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# # check the outcome of out API call
# print(request_bbc_status_code.status_code)
# # lets check the headers
# print(request_bbc_status_code.headers)
# # lets check the content available
# print(request_bbc_status_code.content)

# print the status code with success message
# print unsuccessful if status code is not 200
def request():
    if request_bbc_status_code.status_code == 200:
        print("success")
    else:
        print("unsuccessful")
request()