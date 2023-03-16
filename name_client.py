import requests

server = "http://vcm-21170.vm.duke.edu:5000"

# 1. create a variable containing what we want to send
out_data = {"name": "Hengrui Cai", "net_id": "hc341",
            "e-mail": "hengrui.cai@duke.edu"}
# 2. tell the post request what to send
r = requests.post(server + "/student", json=out_data) #//3.2 post request string is not allowed
print(r.status_code)
print(r.text)

r = requests.get(server + "/list") #3.1 get request can be made in the browser
print(r.text)


# ---------------
input = {"user": "Henry", "message": "Hello bro"} #Posts a message for a specific user. Expects json input: {"user": <user_name>, "message": <message_string>}
r = requests.post("http://vcm-21170.vm.duke.edu:5001/add_message", json=input)

r = requests.get("http://vcm-21170.vm.duke.edu:5001/get_messages/Henry", ) #Retrieves messages for the user indicated by <user_name>.