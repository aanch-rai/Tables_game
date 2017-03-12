from random import *

while True :
	x = int(raw_input("11*11="))
	y = int(raw_input("12*12="))
	z = int	(raw_input("13*13="))
	w = int(raw_input("14*14="))

	if (x==121 and y==144 and z==169 and w==196):
		print "CORRECT!"
		break
	else :
		print "Something is wrong!,Try again!"
	
print "Your time starts now!\n"

import time
time_start = time.time()
time_out = 60				#seconds
correct = 0
wrong = 0
while time.time() < time_start + time_out :
	x = randrange(1,10)
	y = randrange(1,15)
	ans = x*y


	print x,"*",y
	first_inp = raw_input("=")
	if first_inp=="stop":
		break

	elif int(first_inp)==ans:
		print "correct"
		correct = correct + 1
	elif int(first_inp)!=ans :
		print "\n WRONG! \n "
		wrong = wrong + 1
		#wrong[error1] = x,"*",y
	

print "\nWOOPS Your time was up!\n"	
print "No. of correct answers = ",correct
print "No. of wrong answers = ",wrong
