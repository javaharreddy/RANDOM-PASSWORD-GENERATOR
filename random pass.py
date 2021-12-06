import random
asci_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'   
digits='0123456789'           
punctuations="""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'"""    
asci_pref=int(input('do you need abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ in your password\nif yes enter 1 else enter 0 : '))
punctuations_pref=int(input('''do you need !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~  in your password\nif yes enter 1 else enter 0 : '''))
digits_pref=int(input('do you need 0123456789 in your password\nif yes enter 1 else enter 0 : '))
repetition=int(input('do you want repeated characters in your password\nif yes enter 1 else enter 0 : '))
password_generating_string=''
if(asci_pref):
	password_generating_string+=asci_letters
if(punctuations_pref):
	password_generating_string+=punctuations
if(digits_pref):
	password_generating_string+=digits
if(repetition):
	password_generating_string+=password_generating_string+password_generating_string
maxlength=len(password_generating_string)
length_of_the_password=int(input('enter length of the password you need: '))
password=''.join(random.sample(password_generating_string,length_of_the_password))
print("random password with your requirements is: ",password)
