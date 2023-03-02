import requests

r = requests.get("https://api.github.com/repos/dward2/BME547/branches")
print(r)
print(type(r))
print(r.status_code) # whether this request is a good one:  404 doesnot exist/ 200 good one
#make a request douyao check status code

#waht came back from the server
print(r.text)
branches = r.json()
print(branches)
for branch in branches:
    print(branch["name"])

# r = requests.get("")