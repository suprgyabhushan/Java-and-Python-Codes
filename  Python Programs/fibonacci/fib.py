starting, increment = (1, 1)
n=input("enter a number till which you want to print fibonacci series")
while (increment < n):
    print 'The fibo series is {0}'.format(increment)
    starting, increment = (increment, starting + increment)
