import ip
"""
Write a function which takes two argument as_num and lo_ip and give back the Exxon standard ISIS network ID.
Here is the algorithm:

pad loopback IP address with zeros and remove .s.
1.2.3.4 => 001002003004
Take AS number last 4 digits
65123 => 5123
Stick the 1) and 2)
5123001002003004
put a . after every 4 digits
5123.0010.0200.3004
put 49. in from and .00 at the end
49.5123.0010.0200.3004.00
Name the function to to_isis_netid.


# Beginner python - Lesson 3 - homework 3
# ISIS netid
# level: medium
# Hint: use string slicing and functions

"""



def to_isis_netid(as_num, lo_ip):

        #as_num = input("Please give me the AS\n") #("63215")
        #lo_ip = input("Please give me the IP\n") #("150.200.35.45")
        #as_num = "63215"
        #lo_ip = "10.10.10.10"
        lo_ip_list=list()

        splitted_lo_ip=lo_ip.split(".")

        for octet in splitted_lo_ip:
                new_lo_ip=octet.rjust(3, "0")
                lo_ip_list.append(new_lo_ip)
        #print("Started to processing, calculating the value;...")
        #print(lo_ip_list)
        lo_ip_string="".join(lo_ip_list)
        #print(lo_ip_string)
        as_mod=(str)(as_num[-4:])
        #print(as_mod)
        id_together=as_mod + lo_ip_string
        #print(id_together)
        i = 0
        mod_id_together = ""
        for szam in id_together:
                if i==4:
                   mod_id_together +="."
                   i=0
                mod_id_together += szam
                i += 1
        mod_id_together = "49." + mod_id_together + ".00"

        #id_together= "49." + id_together[:4] + "." + id_together[4:8] + "." + id_together[8:12] + "." + id_together[12:16] + ".00"
        #print("\n\nHere is the final ISIS IP based on the given IP and AS:")

        return mod_id_together

as_num = input("AS\n")
#isTheGetIpIsValid = False
#while isTheGetIpIsValid != True:
lo_ip = input("IP\n")
#        isTheGetIpIsValid = ip.ipValidator(lo_ip)
#        if not isTheGetIpIsValid:
#                print("Please give me a valid ip address niga!")

print(to_isis_netid(as_num, lo_ip))


"""
# vsz része
# id_together ezt kell négy karakterenként

result = ""
index = 0
id_together_vsz = "5123001002003004"
for el in id_together_vsz:
        if index > 0 and index%4 == 0:
                result += "."
        result += el
        index += 1
print("VSZ result\n" + result)

print("VSZ2 result\n" )
print(".".join(re.findall("[0-9]{4}", id_together_vsz)))

#end vsz része

"""





"""
def myFunction(num, ip):
        #Todo
        return ""
print(myFunction(input1, unput2))

"""
