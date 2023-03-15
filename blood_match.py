import requests
server = "http://vcm-7631.vm.duke.edu:5002"
getID = requests.get(server + "/get_patients/hc341")
print(getID)
print(type(getID))
print(getID.status_code)
print(getID.text)

donor_blood_type = requests.get(server + "/get_blood_type/F5")
print(donor_blood_type.text)

Recipient_blood_type = requests.get(server + "/get_blood_type/M4")
print(Recipient_blood_type.text)

result = {"Name": "hc341", "Match":  "No"}
r = requests.post(server + "/match_check", json=result)
print(r.status_code)
print(r.text)