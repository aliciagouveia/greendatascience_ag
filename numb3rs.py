import re #re it's for regular expression



def main():
    print(validate(input("IPv4 Address: "))) #we're gonna ask the user for an IP address and check if it's valid


def validate(ip):
    if re.search (r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):   #in the search we need to set the statement and which variable we're looking for(in this case the ip) 
        list_of_ipnumbers = ip.split(".") #os valores do IP serão incorporados numa lista e divididos por pontos
        for number in list_of_ipnumbers: #para cada número na lista só pode estar entre o range de 0 a 255
            if not (0 <= int(number) <= 255) :
                return False
        return True
    else:
        return False
    

...


if __name__ == "__main__":
    main()