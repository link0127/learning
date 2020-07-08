# Beginner router classifier homework
# print only WAN devices!
# Written by Balint Czirjak
"""
devices = [
            "HUBDP-VOIVGW001",
            "HUBDP-VOIVGW002",
            "HUBDP-WANRTC001",
            "HUBDP-WANRTC002",
            "HUBDP-WANRTV001",
            "HUBDP-LANCUA001",
            "HUBDP-LANCUA002",
            "HUBDP-LANCUA003",
            "HUBDP-SECFEL001",
            "HUBDP-SECFIO101",
            "HUBDP-SECFIO101",
            "HUBDP-SECFEC102",
            "HUBDP-SECFEC102"
        ]

# your code comes here
router_pattern = "HUBDP-WAN"

for device in devices:
    if device[:9] == router_pattern:
        print(device)

second_pattern = "WAN"

for device in devices:
    if device[6:9] == second_pattern:
        print(device)

for device in devices:
    if device[6:9] == "WAN":
        print(device)
"""

"""
db = {
    "Router1":"192.168.1.1":"ASNUMBER3",
    "Router2":"172.16.20.20":"ASNUMBER4",
    "Switch1":"10.10.10.1"
     }
print(f"{db}")

"""

# Beginner device database

# Create a more complex data structure where hostnames are keys and every device can have more data

# like IP address, device type and AS number

#

# I am not really interested in real data, rather in how the structure is built up

# Hint: use the data types we learned in this lesson!


db = {
    "router1": {
        "ipaddress": "172.17.0.1",
        "device_type": "router",
        "as_number": "alma"
    },
    "router2": {
        "ipaddress": "172.19.0.1",
        "device_type": "router",
        "as_number": "korte"
    },
    "switch1": {
        "ipaddress": "172.20.0.1",
        "device_type": "switch",
        "as_number": "test"
    }
    }

print(db)
print(type(db))


# Beginner IP address checker

# After input a string from user, respond back if that is an IP address or not!

# example input: 1.1.1.1

# example output: IP

# example input2: whatever

# example output: NOT IP

# Hints: do not overcomplicate! :D

 

# read string from user
"""
s = input("Tell me an IP: ")

# Here comes your code

s = input("Tell me an IP: ")
splitted = s.split(".") ## split function return array
if len(splitted) != 4:
    print("NOT IP")
else:
    print("IP")

"""