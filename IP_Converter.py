from os import system

def main():
    bool = True
    while bool:
        try:
            system("cls")
            banner()
            ip = str(input("IP address : "))
            if IPChecked(ip):
                print()
                break_ip(ip)
                input("\n[^_^] ENTER [^_^]\n")
            else:
                input("\n[!] Invalid IP address [!]\n")
        except ValueError:
            input("\n[!] Invalid IP address [!]\n")

def IPChecked(ip):
    buffer = ""
    if ip.__contains__("."):
        buffer = ip.replace(".","")
        if buffer.isdecimal():
            return True
        else:
            return False
    else:
        return False

def break_ip(ip):
    ip = ip + "{}".format(".")
    length_ip = len(ip)

    ip_list = []

    text = ""

    x = 0
    while x < length_ip:

        if ip[x] == ".":
            x += 1
            ip_list.append(text)
            text = ""
            if x == length_ip:
                continue
        text = text + "{}".format(ip[x])

        x = x + 1

    if len(ip_list) == 4:
        octet1 = int(ip_list[0])
        octet2 = int(ip_list[1])
        octet3 = int(ip_list[2])
        octet4 = int(ip_list[3])

        logicO1 = (octet1 >= 0 and octet1 <= 255)
        logicO2 = (octet2 >= 0 and octet2 <= 255)
        logicO3 = (octet3 >= 0 and octet3 <= 255)
        logicO4 = (octet4 >= 0 and octet4 <= 255)

        if logicO1 and logicO2 and logicO3 and logicO4:
            Binnary(octet1,octet2,octet3,octet4)

        else:
            print("Invalid IP address")


def Binnary(octet1,octet2,octet3,octet4):
    octet1_bin = str(bin((octet1)))
    octet2_bin = str(bin((octet2)))
    octet3_bin = str(bin((octet3)))
    octet4_bin = str(bin((octet4)))

    octet1_bin = octet1_bin[2:]
    octet2_bin = octet2_bin[2:]
    octet3_bin = octet3_bin[2:]
    octet4_bin = octet4_bin[2:]

    length1 = len(octet1_bin)
    length2 = len(octet2_bin)
    length3 = len(octet3_bin)
    length4 = len(octet4_bin)

    # octet1---------------------------------------------
    if length1 == 8:
        print(octet1_bin, end=".")

    else:
        x = length1
        while x < 8:
            octet1_bin = "0" + octet1_bin
            x+=1
        print(octet1_bin,end=".")
    # octet2---------------------------------------------
    if length2 == 8:
        print(octet2_bin, end=".")

    else:
        x = length2
        while x < 8:
            octet2_bin = "0" + octet2_bin
            x+= 1
        print(octet2_bin,end=".")
    # octet3 --------------------------------------------
    if length3 == 8:
        print(octet3_bin, end=".")

    else:
        x = length3
        while x < 8:
            octet3_bin = "0" + octet3_bin
            x+= 1
        print(octet3_bin,end=".")
    # octet4 --------------------------------------------
    if length4 == 8:
        print(octet4_bin)

    else:
        x = length4
        while x < 8:
            octet4_bin = "0" + octet4_bin
            x+= 1
        print(octet4_bin)


def banner():
    banner = """\
    _______________________________________________________________________________________
                          Coded by Majd Frass
    _______________________________________________________________________________________
    	                      ______
    	                   .-"      "-.
    	MAJD              /            \		FRASS
    	                 |              |
    	                 |,  .-.  .-.  ,|
    	            /\   | )(__/  \__)( |
    	          _ \/   |/     /\     \|
    	         \_\/    (_     ^^     _)   .-==/~\\
    	        ___/_,__,_\__|IIIIII|__/__)/   /{~}}
    		---,---,---|-\IIIIII/-|---,\'-' {{~}
    			   \          /     '-==\}/
    	Majd                `--------`                  Frass
    _______________________________________________________________________________________
    Hi everybody I'm Majd Frass and I'm beginner in programming I coded this
    simple code to do convert the ip address from decimal to binnary
    Ex:
    IP address : 192.168.1.1
    11000000.10101000.00000001.00000001
    _______________________________________________________________________________________
    * If you want to exit enter : Exit or ^C
    """
    print(banner)


main()








