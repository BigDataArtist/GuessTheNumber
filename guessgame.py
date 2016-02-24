import random 

GuessTaken = 0

print(" Hello whats your name")

myName = input()

number = random.randint(1,20)

print("Myname is "+myName+' ans i am thinsking of some number between 1 and 20',number)

while GuessTaken < 7:
	print(" Take a guess")
	guess = int(input())
	GuessTaken = GuessTaken+1

	if guess < number:
   		print(" Your guess is too low")

	if guess > number:
		print(" Your nunber is too high")

	if guess == number:
		break

if guess == number:
	print(" good job"+myName+" the number you guessed is right and you got the answer in",GuessTaken,"no of guess")

if guess != number:
	print( " the nunber i was thinking was",number) 	