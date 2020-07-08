
import ipcalc

acl = [
        {'src': '20.0.0.0/16', 'dst': '10.0.0.0/8'},
        {'src': '20.0.0.0/16', 'dst': '20.0.0.0/8'},
        {'src': '10.0.0.0/24', 'dst': '0.0.0.0/0'},
        {'src': '20.0.0.0/16', 'dst': '10.0.0.0/8'},
        {'src': '192.0.0.0/8', 'dst': '10.20.30.0/24'},
        {'src': '50.0.0.0/24', 'dst': '60.0.0.0/24'}
       ]

packet = {'src': '20.0.1.1', 'dst': '20.8.8.8'}
packet0 = {'src': '20.0.1.1', 'dst': '20.8.8.8'}
packet1 = {'src': '10.20.30.40', 'dst': '8.8.8.8'}
packet2 = {'src': '20.0.1.1', 'dst': '10.8.8.8'}
packet3 = {'src': '192.168.0.1', 'dst': '10.20.30.40'}
packet4 = {'src': '195.1.0.1', 'dst': '10.20.30.40'}
packet5 = {'src': '50.0.0.1', 'dst': '60.0.0.99'}

"""
def acl_match(acl, packet):

    for line in acl:
        ACLsource = ipcalc.Network(line["src"])
        if packet["src"] in ACLsource:
            ACLdest = ipcalc.Network(line["dst"])
            IsIPInDSTasWell = packet["dst"] in ACLdest
            break
        else:
            IsIPInDSTasWell = False


    return (IsIPInDSTasWell)
"""


def acl_match(acl, packet):

    IsIPInDSTasWell = True

    for line in acl:
        if packet["src"] in ipcalc.Network(line["src"]):
            IsIPInDSTasWell = packet["dst"] in ipcalc.Network(line["dst"])
            IsIPInDSTasWell = True
            if IsIPInDSTasWell == True:
                break
        else:
            IsIPInDSTasWell = False
    return (IsIPInDSTasWell)

print(acl_match(acl, packet))
print(acl_match(acl, packet0))
print(acl_match(acl, packet1))
print(acl_match(acl, packet2))
print(acl_match(acl, packet3))
print(acl_match(acl, packet4))
print(acl_match(acl, packet5))





"""
We have a standard ACL and a packet with data. Write a function acl_match(acl, packet) and return True if the packet matched the ACL else return False.

input:

acl = [{'src': '10.0.0.0/24', 'dst': '0.0.0.0/0'},
       {'src': '20.0.0.0/16', 'dst': '10.0.0.0/8'},
       ]
packet1 = {'src': '10.1.2.3', 'dst': '8.8.8.8'}
packet2 = {'src': '20.0.1.1', 'dst': '8.8.8.8'}
output:

acl_match(acl, packet1)
True

acl_match(acl, packet2)
False


# Beginner python - Lesson 4 - homework 1

# ACL matcher

# level: easy

# Hint: use ipcalc module (ipcalc.Network, ipcalc.IP but Network is enough)

"""

"""
Here I mention some useful libraries which are not part of standard library set, so you may try these examples on netcsl004.

ipcalc¶
IP calculator builtin :)

ipcalc docs

In [ ]:
# ipcalc example
import ipcalc

ip = ipcalc.IP("1.1.1.1")
net = ipcalc.Network("1.1.1.0", "255.255.255.0")
net2 = ipcalc.Network("2.2.2.0", "255.255.255.0") 

print(ip)
# 1.1.1.1
print(ip in net)
# True
print(ip in net2)
# False
"""