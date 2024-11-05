# https://www.ibm.com/docs/en/order-management-sw/9.3.0?topic=cpms-handling-credit-cards
import math 

while True:
    print("Input a credit card number with no spaces to check if it is valid. \nType 'stop' to stop the program:")
    card_number = input()
    # Examples: 5425233430109903, 4263982640269299, 6011000991300009
    if str(card_number) == "stop":
        break
    
    card_number = abs(int(card_number))
    print("Card Number: "+str(card_number))
    
    str_card_number = str(card_number)
    
    card_split = []
    card_split[:] = str(card_number)
    
    def luhn_check(num_list, length):
        #Luhn's Algorithm
        if length == 13:
            #6
            step_one = str(int(str_card_number[11])*2) + str(int(str_card_number[9])*2) + str(int(str_card_number[7])*2) + str(int(str_card_number[5])*2) + str(int(str_card_number[3])*2) + str(int(str_card_number[1])*2)
            
            luhn_split = []
            luhn_split[:] = step_one
            
            sum_luhn = 0
            for i in luhn_split:
                sum_luhn += int(i)
                
            step_two = int(str_card_number[12])+int(str_card_number[10])+int(str_card_number[8])+int(str_card_number[6])+int(str_card_number[4])+int(str_card_number[2])+int(str_card_number[0])
            
            total_sum = sum_luhn+step_two
            
            if total_sum % 10 == 0:
                print("This card is Valid! It passed the Luhn test.")
                print("")
            else:
                print("This card is not Valid.")
                print("")
        elif length == 15:
            #7
            step_one = str(int(str_card_number[13])*2) + str(int(str_card_number[11])*2) + str(int(str_card_number[9])*2) + str(int(str_card_number[7])*2) + str(int(str_card_number[5])*2) + str(int(str_card_number[3])*2) + str(int(str_card_number[1])*2)
    
            luhn_split = []
            luhn_split[:] = step_one
            
            sum_luhn = 0
            for i in luhn_split:
                sum_luhn += int(i)
                
            step_two = int(str_card_number[14])+int(str_card_number[12])+int(str_card_number[10])+int(str_card_number[8])+int(str_card_number[6])+int(str_card_number[4])+int(str_card_number[2])+int(str_card_number[0])
            
            total_sum = sum_luhn+step_two
            
            if total_sum % 10 == 0:
                print("This card is Valid! It passed the Luhn test.")
                print("")
            else:
                print("This card is not Valid.")
                print("")
        elif length == 16:
            #8
            step_one = str(int(str_card_number[14])*2) + str(int(str_card_number[12])*2) + str(int(str_card_number[10])*2) + str(int(str_card_number[8])*2) + str(int(str_card_number[6])*2) + str(int(str_card_number[4])*2) + str(int(str_card_number[2])*2) + str(int(str_card_number[0])*2)
    
            luhn_split = []
            luhn_split[:] = step_one
            
            sum_luhn = 0
            for i in luhn_split:
                sum_luhn += int(i)
                
            step_two = int(str_card_number[15])+int(str_card_number[13])+int(str_card_number[11])+int(str_card_number[9])+int(str_card_number[7])+int(str_card_number[5])+int(str_card_number[3])+int(str_card_number[1])
            
            total_sum = sum_luhn+step_two
            
            if total_sum % 10 == 0:
                print("This card is Valid! It passed the Luhn algorithm.")
                print("")
            else:
                print("This card is not Valid.")
                print("")
    
    #Checks if card number has the correct number of digits
    if len(str_card_number) == 13 or len(str_card_number) == 15 or len(str_card_number) == 16:
        print("Number of digits: "+str(len(str_card_number)))
        
        #American Express
        if card_split[0] == "3":
            if card_split[1] == "4" or card_split[1] == "7":
                network_name = "American Express"
    
        #MasterCard
        elif card_split[0] == "5":
            network_name = "MasterCard"
    
        #Visa
        elif card_split[0] == "4":
            network_name = "Visa"
        
        #Discover
        elif str_card_number[:4] == "6011":
            network_name = "Discover"
            
        else:
            network_name = "Other"
        
        print("Type of Payment Network: "+str(network_name)) 
            
        luhn_check(str_card_number,len(str_card_number))
            
    else:
        print("Please enter a valid credit card with 13, 15 or 16 digits.")
        print("")