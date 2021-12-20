# function which is reponsible for reading the input file
def readAccounts(infile):
    name_account = {}
    # read one line from the file each time
    while True:
        line = infile.readline().strip()
        if line:
            # try if the account is valid
            try:
                float(line.split(':')[1])
            except ValueError:
                print("ValueError. Account for %s not added: illegal value for balance" % (line.split(':')[0]))
            else:
                name_account[line.split(':')[0]] = float(line.split(':')[1])
        # if the encounters empty line, then stop reading
        else:
            break
    return name_account


# function which is responsible for processing accounts
def processAccounts(accounts):
    #print(accounts)
    name = input("Enter account name, or 'Stop' to exit: ")
    if name == "Stop":
        return "Stop"
    # try if the imput name is valid
    try:
        accounts[name]
    # if the name is not included in the dictionary
    except KeyError:
        print("KeyError. Account for %s does not Exist. Transaction cancelled." %(name))
    else:
        amount_value = input("Enter transaction amount for %s: " % (name))
        # try if the input value is valid
        try:
            float(amount_value)
        # if the input value is not valid
        except ValueError:
            print("Value Error. Incorrect Amount. Transaction cancelled.")
        else:
            accounts[name] += float(amount_value)
            print("New balance for account %s: %s" %(name, accounts[name]))


# main function which is responsible for calling other functions
def main():
    file_name = input("Enter filename> ")
    # try if the file exist or not
    try:
        file = open(file_name, 'r')
    # if the file does not exist
    except IOError:
        print("IOError. %s does not exist" %(file_name))
    # if the file exist
    else:
        accounts = readAccounts(file)
        while True:
            if processAccounts(accounts) == "Stop":
                break
        file.close()


main()