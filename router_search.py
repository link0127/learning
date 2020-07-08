
#
# Beginner router classifier homework
# print only WAN devices!
# Written by Balint Czirjak

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

needed_routers = "HUBDP-WANRTC001"

for routers_result in devices:
    if routers_result == needed_routers:
        print(f"{routers_result}")
        break
else:
    print ("There is no router found on the list")


