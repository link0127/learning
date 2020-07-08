"""
I prepared a very basic connectivity and pinging functionality. Now we can ping between connected interfaces!

Your task is to complete this program with these abilities:

Create a Router class inherited from Device
Implement possibility to specify interfaces by constructor (for example: ['g0/0','g0/1','g0/2'])
Implement possibility to configure IP for interfaces runtime by console commands (no need conf t, but would be fancy)
Implement show ip interface brief command to list configured IPs
Ability to specify ping count by the command. Like: ping -c 5 x.x.x.x OR ping repeat 5 x.x.x.x
You can do it by the Router or base Device. I don't care.
You have free hands! I only expect basic functionality and not Cisco quality inputs/outputs.
Of course pretty, funny and cool stuff is always a BONUS!!!!!!

"""


# Beginner python - Lesson 8 - homework 2
# GNS2
# level: hard
from ipcalc import IP, Network
from time import sleep
import re


class Device:
    """
    This is a general device class
    """

    # class attributes. These are default values only which can be overriden later!
    devicetype = "generic network device"
    registered = set()

    # Constructor creates instance attributes
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = IP(ip)
        self.interfaces = {'eth0': {'ip': self.ip, 'connected': None}}
        # add a functionality to stop instantiating in case this IP was already created
        if ip in self.registered:
            raise Exception(f'This device ({ip}) is already registered!')
        else:
            self.registered.add(ip)

    def description(self):
        print(f"This is {self.hostname}, a {self.devicetype}.")

    def connect(self, interface: str, remote_device: 'Device', remote_interface: str):
        """
        Connect device interface to another device interface
        :param interface: specify interface name on this device
        :param remote_device: specify remote device
        :param remote_interface: specify remote device interface name
        :return: None
        """
        # connect cable on our side
        self.interfaces[interface]['connected'] = {'device': remote_device, 'interface': remote_interface}
        # connect cable on the other side
        remote_device.interfaces[remote_interface]['connected'] = {'device': self, 'interface': interface}

    def console_service(self):
        """
        Implements CLI access to this device
        :return:
        """
        while True:
            # parse command from CLI (command, args)
            m = re.findall(r"^(\w+) ?(.*)", input(f"{self.hostname}# "))
            if m:
                command, args = m[0]  # findall pass first match as (match1, match2)
            else:
                continue
            if command == "exit":
                print("Goodbye!")
                return
            if command == "help":
                print("\n".join(("help     : Print help",
                                 "ping -c 3 [ip]: Ping the ip",
                                 "conf [interface] [ip]: Configure interface IP address",
                                 "lsi: List interface with ip",
                                 "exit     : Exit console"
                                )))
            if command == "ping":
                self.echo(args)
            if command == "conf":
                self.configure(args)
            if command == "lsi":
                self.lsi()

    def lsi(self):
        for name, data in self.interfaces.items():
            print("Interface: " + name + " - IP: " + (str)(data['ip']))

    def configure(self, args: str):
        interface, ip = args.split(" ")
        if interface in self.interfaces:
            ip = IP(ip)
            self.interfaces[interface]['ip'] = ip
            print("Interface ip successfully assigned to " + interface)
        else:
            print("This is not a valid interface name")

    def echo(self, ip: str) -> None:
        """
        Send ping echo request to destination
        :param ip: destination IP
        :return: None
        """
        ip_count = 5
        args = ip.split(" ")
        if len(args) == 3:
            if args[0] == "-c":
                ip_count = (int)(args[1])
                ip = args[2]
        elif len(args) == 1:
            ip = args[0]

        # convert str to IP address object
        ip = IP(ip)
        # iterate over all interfaces on device to find connected route
        #print(self.interfaces)
        for name, data in self.interfaces.items():
            # print(name)
            # find connected interface by checking if destination IP is included in our interface subnets
            if ip in Network(data['ip']):  # so I convert IP/nm to a Network to be able to use 'in' for checking
                # no link (connected device)
                if data['connected'] is None:
                    print(f'Error - interface link down on {name}')
                    return
                # there is link, try to ping
                if 'device' in data['connected']:
                    print(f'Pinging {ip}...')
                    for n in range(ip_count):
                        # Pinging ourselves... is fast :)
                        if data['ip'] == ip:
                            print('!', end='')
                            continue
                        reply = data['connected']['device'].echo_reply(ip)  # call echo-reply with destination IP
                        if reply == "!":  # the other end sent back '!' which means destination IP is there
                            print("!", end='')
                            sleep(0.100)  # simulate network response time
                        else:             # the other end did not send '!' so there is a problem over there
                            print(".", end='')
                            sleep(1)      # simulate timeout :)
                    print()
                    return
        print(f'Error - no route to {ip}')

    def echo_reply(self, ip: IP) -> str:
        """
        Reply to ping echo packets
        :param ip: destination IP
        :return: "!" on good IP, else ""
        """
        for name, data in self.interfaces.items():
            if ip == data['ip']:
                # other end pinged our IP, so reply "!" as ok
                if data['connected'] != None :
                    if 'device' in data['connected']:
                        return "!"
        # we did not found our IP in the request, return empty string
        return ""


class Server(Device):
    """
    Generic server class
    """
    # overriding class attribute
    devicetype = "generic server"




class Router(Device):
    # overriding class attribute
    devicetype = "router"

    def __init__(self, hostname, configs):
        self.interfaces = {}
        self.hostname = hostname
        for config in configs:
            ip = IP(config['ip'])
            self.interfaces[config['interface']] = {'ip': ip, 'connected': None}
            if ip in self.registered:
                raise Exception(f'This device ({ip}) is already registered!')
            else:
                self.registered.add(ip)


# this is a basic console connection function :)
def console_to(device: Device):
    device.console_service()

# create server objects
netcsl1 = Server('netcsl001', '1.1.1.1/24')
netcsl2 = Server('netcsl002', '1.1.1.2/24')
netcsl3 = Server('netcsl003', '1.1.1.5/24')

# create router object
configom = [
    {'interface': "g0/0", 'ip': "1.1.1.3/24"},
    {'interface': "g0/1", 'ip': "1.1.1.4/24"}
]

router1 = Router('router1', configom)

# connect netcsl1 to netcsl2 over eth0 interfaces
netcsl1.connect('eth0', netcsl2, 'eth0')
router1.connect('g0/0', netcsl2, 'eth0')
router1.connect('g0/1', netcsl2, 'eth0')

print(router1.interfaces)

# console in to netcsl1
console_to(router1)
# you can try commands like: help, ping 1.1.1.2, exit