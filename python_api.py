# APIs with python
# install requests
# pip install requests

import requests
# get
#request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")
# # check the outcome of out API call
# print(request_bbc_status_code.status_code)
# # lets check the headers
# print(request_bbc_status_code.headers)
# # lets check the content available
# print(request_bbc_status_code.content)

# print the status code with success message
# print unsuccessful if status code is not 200
# def request():
#     if request_bbc_status_code.status_code == 200:
#         print("success")
#     else:
#         print("unsuccessful")
# request()



# valid post-code or invalid - url of the API address
url = "http://api.postcodes.io/postcodes/"
# store the data
# user input as postcode
postcode = input("enter postcode: ")
url_arg = url + postcode
#print(f"your postcode is {postcode}")
response = requests.get(url_arg)
response_dict = response.json()
#print(response_dict)
#print(response_dict["result"]["longitude"])
# print(response_dict["result"]["latitude"])

def postcode_check(postcode):
    request_postcode = requests.get(url + postcode)
    if request_postcode.status_code == 200:
        return "postcode valid"
    else:
        return "postcode invalid "
print(postcode_check(postcode))















