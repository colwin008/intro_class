def tip (bill_amount, tip_percentage):
    return bill_amount * tip_percentage / 100

def total_bill (bill_amount, tip):
    return bill_amount + tip

def split_amount (total_bill, number_of_people):
    return total_bill / number_of_people


def main():
    choice = raw_input("Do you want to 1 - Calculate Tip or 2 - Split the bill?")
    if choice == "1":
        bill_amount = float(raw_input("What is the original bill amount?"))
        tip_percentage = float(raw_input("What is the tip percentage?"))
        print "tip amount is" , tip_percentage, "bill total is", bill_amount
        split_bill = raw_input("World you like to split the bill?")
        if split_bill == "Yes":
            number_of_people = int(raw_input("How many people do you have?"))
            the_tip = tip(bill_amount, tip_percentage) 
            print split_amount(total_bill(bill_amount, the_tip), number_of_people)
        elif split_bill == "No":
            the_tip = tip(bill_amount, tip_percentage)
            print "Your total bill is", total_bill(bill_amount, the_tip)  
    if choice == '2':
        total_bill_amount = float(raw_input("What is the total bill amount?"))
        people = int(raw_input ("How many people do you have?"))
        print "the cost per person is", split_amount(total_bill_amount, people)


if __name__=='__main__':
    main()
