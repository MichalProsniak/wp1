#string.ascii_letters # Concatenation of the ascii (upper and lowercase) letters
#string.ascii_lowercase # All lower case letters
#string.ascii_uppercase # All Upper case letters
#string.digits  # The string ‘0123456789’.
#string.punctuation  # String of ASCII characters which are considered special characters.
#You can concatenated strings you need and choose a random character using:
#random.choice(string_with_all_characters)



'''
import string    
import random 
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
all_characters = lowercase + uppercase + digits + punctuation

print ("Set password lenght")
password_lenght = int(input())

 
password = '' .join(random.choices(all_characters, k = password_lenght))    
print("The randomly generated password is : " + str(password)) # print the random data  

resoults = ''
for i in range (password_lenght):
    sign = random.choice(all_characters)
    resoults += ord(sign)
print (resoults)
'''
import string
import random
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
all_characters = lowercase + uppercase + digits + punctuation
def password_generator():

    print ("Set password lenght")
    password_lenght = int(input())

    print('Your password:')

    resoults = []
    for i in range (password_lenght):
        sign = random.choice(all_characters)
        resoults.append(sign)

    password = ''
    for ele in resoults:
        password += ele
    print(password)

password_generator()





