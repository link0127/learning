"""
import random
input_szam=input("Adj meg egy számot én tuti nagyobbat mondok\n")

InToString=(float)(input_szam)
print(type(InToString))

generated_szam=random.uniform(InToString+0.1, InToString*2)
print("{:.0f}".format(generated_szam));

"""

def ipValidator(input_ip):
    ip = input_ip.split(".")
    validip = True
    octet_counter = 0

    if len(ip) == 4:
        for given_octet in ip:
            if given_octet.isnumeric() == False:
                validip = False
                break
            else:
                octet_counter += 1
                ip_int = int(given_octet)
                if octet_counter == 1:
                    if ip_int <= 0 or ip_int > 255:
                        validip = False
                        break
                else:
                    if ip_int > 255 or ip_int < 0:
                        validip = False
                        break
    else:
        validip = False

    return validip

def infinitiIpValidator ():

    input_ip=str()
    historycalCount = 0
    historycal_stored = dict()

    file = open("ip.txt", "w")
    file.close()

    while input_ip!="exit":
        input_ip = input('Please give me an IP address, I will tell whether it is valid or not. If you wish to stop the program type the word "exit".\n')
        historycalCount +=1

        if input_ip == "exit":
            exit(0)
        else:
            ip=input_ip.split(".")
            validip=True
            octet_counter=0

            if len(ip) == 4:
                for given_octet in ip:
                    if given_octet.isnumeric() == False:
                        validip=False
                        break
                    else:
                        octet_counter +=1
                        ip_int = int(given_octet)
                        if octet_counter==1:
                            if ip_int<=0 or ip_int>255:
                                validip=False
                                break
                        else:
                            if ip_int>255 or ip_int<0:
                                validip=False
                                break
            else:
                validip=False

            #tömbben tárolás - HISTORYCAL DATA
            #row_historycal_data = {historycalCount: {input_ip : validip}}
            #historycal_stored.update(row_historycal_data)
            #print(historycal_stored)

            #fájblan tárolás: - HISTORYCAL DATA

            StoreToFile = input_ip + " : " + str(validip) + "\n"
            file = open("ip.txt", "a")
            file.write(StoreToFile)
            file.close()

            file = open("ip.txt", "r")
            print(file.read())


            if validip==True:
                print("This is a valid IP.")
            else:
                print("This is not a valid IP")