
def main():
    num=(30/5)
    print (num, type(num))
    num = float(30 / 5)  # changing the type from int to float
    print (num, type(num))

    data = "My name is Mohamed"
    print (data, type(data))
    data="My \n name is \n Mohamed"
    print(data,type(data))

    Amount=30
    data="{} is high".format(Amount)
    print(data, type(data))
    print (len(data)) #printing the length of a string
    print data[0] #printing one character of a string
    print "**********"
    print data[6] #printing one character of a string


if __name__ == '__main__':main()