# Read data from 'families.txt'
families_file = open('families.txt', 'r')
families_data = families_file.read()
families_file.close()
# families_phonenumber: Dictionary like {"Phonenumber":"Families Name"..}
families_phonenumber = {}
# families.split(',')[0]: Phonenumber
# families.split(',')[1]: Families Name
for families in families_data.splitlines():
    families_phonenumber[families.split(',')[0]] = families.split(',')[1]
for phonenumber in families_phonenumber:
    families_name = families_phonenumber[phonenumber]
    families_phonenumber[phonenumber] = families_name[0:18]




# Read data from 'dues.txt'
dues_file = open('dues.txt', 'r')
dues_data = dues_file.read()
dues_file.close()
# dues_phonenumber: Dictionary like {"Phonenumber": [Total Dues]..}
dues_phonenumber = {}
# due_date_phone.split(';')[2]: Phonenumber
for due_date_phone in dues_data.splitlines():
    dues_phonenumber[due_date_phone.split(';')[2]] = []
for due_date_phone in dues_data.splitlines():
    for phone in dues_phonenumber.keys():
        if due_date_phone.split(';')[2] == phone:
            # due_date_phone.split(';')[1]: Dues
            dues_phonenumber[phone].append(due_date_phone.split(';')[1])
# Calculating total dues
for phone in dues_phonenumber.keys():
    sum_of_due = 0
    for dues in dues_phonenumber[phone]:
        sum_of_due += float(dues)
    dues_phonenumber[phone].clear()
    dues_phonenumber[phone].append(sum_of_due)




# Read data from 'payments.txt'
payments_file = open('payments.txt')
payments_data = payments_file.read()
payments_file.close()
# payments_date_phonenumber: Dictionary like {"Phonenumber":[["Date, Payment"]..]..}
payments_date_phonenumber = {}
# totalpay_phonenumber: Dictionary like {"Phonenumber": Total Payment}
totalpay_phonenumber = {}
for pay_date_phone in payments_data.splitlines():
    # pay_date_phone.split(';')[2]: Phonenumber
    payments_date_phonenumber[pay_date_phone.split(';')[2]] = []
for pay_date_phone in payments_data.splitlines():
    for phone in payments_date_phonenumber.keys():
        if pay_date_phone.split(';')[2] == phone:
            # pay_date_phone.split(';')[0]: Date
            # pay_date_phone.split(';')[1]: Payment
            payments_date_phonenumber[phone].append([pay_date_phone.split(';')[0], pay_date_phone.split(';')[1]])
# Calculating total payment
for phone in payments_date_phonenumber.keys():
    total_payment = 0
    for j in range(len(payments_date_phonenumber[phone])):
        total_payment += float(payments_date_phonenumber[phone][j][1])
    totalpay_phonenumber[phone] = total_payment




# Determine all the families and their phone numbers which need to be printed
# on the output table
# related_phonenumbers: List contains all the phonenumbers which appears
# in payment.txt or dues.txt
related_phonenumbers = []
for phonenumber in dues_phonenumber.keys():
    related_phonenumbers.append(phonenumber)
for phonenumber in payments_date_phonenumber.keys():
    if phonenumber not in related_phonenumbers:
        related_phonenumbers.append(phonenumber)
# Sort the list
related_phonenumbers.sort()




# Calculate total dues and interests
# totaldues_interest_phonenumber: Dictionary like {"Phonenumber": [Total Dues, Interests]}
totaldues_interest_phonenumber = {}
for phone in related_phonenumbers:
    totaldues_interest_phonenumber[phone] = [0]
    # If the phonenumber is reltaed to dues, add it to total dues
    if phone in dues_phonenumber.keys():
        due = float(dues_phonenumber[phone][0])
        totaldues_interest_phonenumber[phone][0] += due
    # If the phonenumber is reltaed to payments, minus its payment from its dues
    if phone in payments_date_phonenumber.keys():
        for date_pay in payments_date_phonenumber[phone]:
            totaldues_interest_phonenumber[phone][0] -= float(date_pay[1])
    # If the phonenumber have interest, then calculate it interest
    if totaldues_interest_phonenumber[phone][0] > 100:
        interest = totaldues_interest_phonenumber[phone][0] * 0.01
        totaldues_interest_phonenumber[phone] = [totaldues_interest_phonenumber[phone][0] + interest, interest]
# Calculate total dues after minusing payment and adding interest
total_dues = 0
total_interest = 0
for dues in totaldues_interest_phonenumber.values():
    # If has no interest
    if len(dues) == 1:
        total_dues += dues[0]
    # If has interest
    elif len(dues) == 2:
        total_dues += dues[0]
        total_interest += dues[1]




# Creat a new file called "summary.txt"
summary_file = open('summary.txt', 'w')
# Print the output table according to requirement
summary_file.write("+--------------+------------------+--------+-----+\n")
summary_file.write("| Phone Number | Name             | Due    | Int |\n")
summary_file.write("+--------------+------------------+--------+-----+\n")

for i in range(len(related_phonenumbers)):
    phone = related_phonenumbers[i]
    first_three_digits = phone[0] + phone[1] + phone[2]
    middle_three_digits = phone[3] + phone[4] + phone[5]
    last_four_digits = phone[6] + phone[7] + phone[8] + phone[9]
    # If the customer have interest
    if len(totaldues_interest_phonenumber[phone]) == 2:
        # If the customer will not be provided credit purchase
        if totaldues_interest_phonenumber[phone][0] >= 500:
            # If the customer have made payments
            if phone in payments_date_phonenumber.keys():
                summary_file.write("|(%s) %s %s|**%-16s|$%7.2f|$%4.2f| " \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone][0:16], \
                                    totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
                summary_file.write("[$%.2f] " %(totalpay_phonenumber[phone]))
                for k in range(len(payments_date_phonenumber[phone])):
                    summary_file.write(payments_date_phonenumber[phone][k][0])
                    summary_file.write(" ")
                    if k >= 0 and k < (len(payments_date_phonenumber[phone]) - 1):
                        summary_file.write("($%.2f); " %(float(payments_date_phonenumber[phone][k][1])))
                    if k == len(payments_date_phonenumber[phone]) - 1:
                        summary_file.write("($%.2f);\n" %(float(payments_date_phonenumber[phone][k][1])))
            # If the customer have not made any payments
            else:
                summary_file.write("|(%s) %s %s|**%-16s|$%7.2f|$%4.2f|\n" \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone][0:16], \
                                    totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
        # If the customer can still make credit purchase
        else:
            # If the customer have made payments
            if phone in payments_date_phonenumber.keys():
                summary_file.write("|(%s) %s %s|%-18s|$%7.2f|$%4.2f| " \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                                    totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
                summary_file.write("[$%.2f] " %(totalpay_phonenumber[phone]))
                for k in range(len(payments_date_phonenumber[phone])):
                    summary_file.write(payments_date_phonenumber[phone][k][0])
                    summary_file.write(" ")
                    if k >= 0 and k < (len(payments_date_phonenumber[phone]) - 1):
                        summary_file.write("($%.2f); " %(float(payments_date_phonenumber[phone][k][1])))
                    if k == len(payments_date_phonenumber[phone]) - 1:
                        summary_file.write("($%.2f);\n" %(float(payments_date_phonenumber[phone][k][1])))
            # If the customer have not made any payments
            else:
                summary_file.write("|(%s) %s %s|%-18s|$%7.2f|$%4.2f|\n" \
                                  %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                                  totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
    
    # If the customer have no interest
    elif len(totaldues_interest_phonenumber[phone]) == 1:
        # If the customer will not be provided credit purchase
        if totaldues_interest_phonenumber[phone][0] >= 500:
            # If the customer have made payments
            if phone in payments_date_phonenumber.keys():
                summary_file.write("|(%s) %s %s|**%-16s|$%7.2f|     | " \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                                    totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
                summary_file.write("[$%.2f] " %(totalpay_phonenumber[phone]))
                for k in range(len(payments_date_phonenumber[phone])):
                    summary_file.write(payments_date_phonenumber[phone][k][0])
                    summary_file.write(" ")
                    if k >= 0 and k < (len(payments_date_phonenumber[phone]) - 1):
                        summary_file.write("($%.2f); " %(float(payments_date_phonenumber[phone][k][1])))
                    if k == len(payments_date_phonenumber[phone]) - 1:
                        summary_file.write("($%.2f);\n" %(float(payments_date_phonenumber[phone][k][1])))              
            # If the customer have not made any payments
            else:
                summary_file.write("|(%s) %s %s|**%-16s|$%7.2f|     |\n" \
                      %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                        totaldues_interest_phonenumber[phone][0], totaldues_interest_phonenumber[phone][1]))
        # If the customer can still make credit purchase
        else:
            # If the customer have made payments
            if phone in payments_date_phonenumber.keys():
                summary_file.write("|(%s) %s %s|%-18s|$%7.2f|     | "  \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                                    totaldues_interest_phonenumber[phone][0]))
                summary_file.write("[$%.2f] " %(totalpay_phonenumber[phone]))
                for k in range(len(payments_date_phonenumber[phone])):
                    summary_file.write(payments_date_phonenumber[phone][k][0])
                    summary_file.write(" ")
                    if k >= 0 and k < (len(payments_date_phonenumber[phone]) - 1):
                        summary_file.write("($%.2f); " %(float(payments_date_phonenumber[phone][k][1])))
                    if k == len(payments_date_phonenumber[phone]) - 1:
                        summary_file.write("($%.2f);\n" %(float(payments_date_phonenumber[phone][k][1])))
            # If the customer have not made any payments
            else:
                summary_file.write("|(%s) %s %s|%-18s|$%7.2f|     |\n" \
                                   %(first_three_digits, middle_three_digits, last_four_digits, families_phonenumber[phone], \
                                    totaldues_interest_phonenumber[phone][0]))                

summary_file.write("+--------------+------------------+--------+-----+\n")
summary_file.write("| Total Dues   |                $%10.2f|\n" %(total_dues))
summary_file.write("+--------------+---------------------------+\n")
summary_file.write("| Total Interes|                  $%8.2f|\n" %(total_interest))
summary_file.write("+--------------+---------------------------+")
summary_file.close()

# Read the file "summary.txt" again and print the table contained in the file
screen_output_file = open('summary.txt', 'r')
screen_output = screen_output_file.read()
for table in screen_output.splitlines():
    print(table)