"""
def adder(*args):
    numbers = args
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(adder(1,2,3))


def greet(**kwargs):
    if 'last_name' in kwargs:
        print(f"Hello Mr. {kwargs['last_name']}!")
    elif 'first_name' in kwargs:
        print(f"Hello {kwargs['first_name']}!")


greet(first_name="Viktor")
greet(last_name="Kertesz", first_name="Viktor")
greet(asdasd="Viktor")


def argprint(**kwargs):
    for var in kwargs.keys():
        print(f"{var}: {kwargs[var]}")


argprint(arg1='arg1', arg2=2, arg3=[1, 2, 3])

"""
"""
# basic connectivity with netmiko
#
# import handler for maintaining connectiviy
from netmiko import ConnectHandler

# nice package to securely read password and find out username
from getpass import getuser, getpass


def main():
    user = "cisco"
    password = "cisco"
    port = 5000

    if not user:
        user = getuser()  # this will ask OS to provide login id. LANID most of the time.
    if not password:
        password = getpass(f"Password for {user}: ")  # ask password without echoing it!
    if not port:
        port = input("Port number: ")

    # prepare connection attributes
    gns3_host = {'device_type': 'cisco_ios_telnet',  # configure netmiko to use telnet for IOS connection
                 'host': '127.0.0.1',  # device IP/hostname
                 'port': 5000,  # device listens on this port
                 'username': "cisco",  # login username if device prompts for one
                 'password': "cisco",  # login password if device prompts for one
                 }
    # connecting to device with the above parameters. Of course we could specify those as parameters here,
    # but we have so many options, it would ruin the code readability.
    gns3 = ConnectHandler(fast_cli=True, **gns3_host)

    # in order to see something we ask netmiko to get the prompt for us
    prompt = gns3.find_prompt()
    print(prompt)


    # get all interface configuration
    interfaces = gns3.send_command("show run | s ip")
    print(interfaces)


if __name__ == "__main__":
    main()
"""
"""

In
this
homework
I
ask
you
to
implement
a
ZTP(zero
touch
provisioning) of
network
devices.You
should
use
GNS3 and create
this
topology: image.png

Task is to
develop
a
program
which
will
configure
devices
with those given IPs and make it possible to ping each other:

R1  # ping 2.2.2.2
R2  # pint 1.1.1.1
Base
config
of
the
routers
should
be
empty!!! No
need
to
write
memory
to
be
able
to
test
quickly
by
rebooting
the
routers...
"""
# Beginner python - Lesson 9 - homework 1
# Animal basic automation
# level: medium
# hint: use ipcalc as above. no need for jinja2. keep it simple!
#       also you may do the configuration by hand first to know what to do!
from netmiko import ConnectHandler
import ipcalc

# complete the following data structure
# you'll use it as source of configuration data
ZTP_DATA = {
    'R1': {
        'interfaces': {
            'lo0':  {'ip': '1.1.1.1/32'},
            'fa0/0': {'ip': '10.0.12.1/29'}
                    },
        'routes': {
            'destination': "2.2.2.2",
             'nexthop': "10.0.12.2"
        }
        },
    'R2': {
            'interfaces': {
                'lo0':  {'ip': '2.2.2.2/32'},
                'fa0/0': {'ip': '10.0.12.2/29'}
                        },
            'routes': {
                'destination': "1.1.1.1",
                 'nexthop': "10.0.12.1"
            },
    }
}


def checkBefore(device):
    # check before config
    print("Before configuration:\n")
    print("*" * 40 + "\n")
    print(device.send_command("show ip int brief"))
    print(device.send_command("show run int fa0/0"))
    print(device.send_command("show ip route"))
    print("*" * 40 + "\n")

def checkAfter(device):
    # read config again for validation
    print("After configuration:\n")
    print("*" * 40 + "\n")
    print(device.send_command("show ip int brief"))
    print(device.send_command("show run int fa0/0"))
    print(device.send_command("show ip route"))
    print("*" * 40 + "\n")

def ztp_on_console(device, data):

    #start configuring the device
    print("Configuring device...")

    networkconvert = ipcalc.Network(data['interfaces']['lo0']['ip'])
    network = networkconvert.netmask()
    networkconvert = str(network)

    ip = data['interfaces']['lo0']['ip'].split("/")
    pureIP = ip[0]
    ipconvert = str(pureIP)

   #this is a duplicatum, would be better to define a function here insted of duplicating
    networkconvert_fa = ipcalc.Network(data['interfaces']['fa0/0']['ip'])
    network_fa = networkconvert_fa.netmask()
    networkconvert_fa = str(network_fa)

    ip = data['interfaces']['fa0/0']['ip'].split("/")
    pureIP_fa = ip[0]
    ipconvert_fa = str(pureIP_fa)

    config_loopback = ("interface loopback0 " + "\n" + "ip address " + ipconvert + " " + networkconvert + "\n" + "no shut" + "\n")
    config_uplink = ("interface fa0/0 " + "\n" + "ip address " + ipconvert_fa + " " + networkconvert_fa + "\n" + "no shut" + "\n")
    config_routes = ("ip route " + data['routes']['destination'] + " " + "255.255.255.255 " + data['routes']['nexthop'] + "\n")
    config = config_loopback + config_uplink + config_routes
    print(config)

    push = config.split("\n")
    device.send_config_set(push)

def main():
    R1_port = 5000  # might need update based on your GNS3 setup
    R1 = ConnectHandler(fast_cli=True, host='127.0.0.1', port=R1_port, device_type='cisco_ios_telnet')

    # check before config
    checkBefore(R1)

    # call the above function to configure R1
    ztp_on_console(R1, ZTP_DATA['R1'])

    checkAfter(R1)
    #read config again for validation

    R2_port = 5001  # might need update based on your GNS3 setup
    R2 = ConnectHandler(fast_cli=True, host='127.0.0.1', port=R2_port, device_type='cisco_ios_telnet')

    # check before config
    checkBefore(R2)

    # call the above function to configure R2
    ztp_on_console(R2, ZTP_DATA['R2'])

    checkAfter(R2)
    #read config again for validation

    print(R1.send_command('ping 2.2.2.2'))
    print(R2.send_command('ping 1.1.1.1'))

if __name__ == '__main__':
    main()