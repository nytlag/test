# Altyn Gylyjova 
import sys 

# this will print asterisks 
def print_triangle (n):
	for i in range (n):
		print "*",
	
	print (" ")

# save prompt messages
yes_reply ="y"
no_reply = "n"
answer=" "

# function prints prompt message

def prompt_message():
	flag1=1	
	while (flag1):
		answer1 = raw_input('Would you like to play again? Please enter yes or no:  ')
		answer=answer1.lower()
			
		if answer == yes_reply:
			get_positive_integer()

		elif (answer == no_reply):
			print "thank you for playing"
			flag1=0
			sys.exit()
		else:
			print "wrong answer"


# function reads user input for an number

def get_positive_integer():
    flag=1
    while (flag):
        number = int(input('Enter positive integer: '))
        
        if (number >0):
          flag=0
          print_triangle(number)
        else:
        	print ("please enter valid number")


#print (sys.version_info)
get_positive_integer()
prompt_message()