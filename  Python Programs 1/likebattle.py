import random

guesses_made = 1

name = raw_input('Hello! What is your name?\n')

number = random.randint(1, 20)
print 'Well, {0}, I am thinking of a number between 1 and 20.'.format(name)

while guesses_made < 6:

    guess = int(raw_input('Take a guess: '))

    if guess == number:
    	break

    else:
   	 
    	 elif guess < number:
        	print 'Your guess is too low.'
		i="a"
		if i=="a" :
			print 'guess a new number'

    
	

    	 elif guess > number:
        	print 'Your guess is too high.'
		i="a"
    				
    
    guesses_made += 1

if guess == number:
    print 'Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made)
else:
    print 'Nope. The number I was thinking of was {0}'.format(number)
