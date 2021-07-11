def check_if_prime(n):
    print(str(n) + " ")
    isPrime = True
    for j in range(2,n):
        if n%j == 0: # MOD == 0 MEANS NO REMINDER
            isPrime = False

    if isPrime:
        print("I am Prime! :) ")
    else:
        print("I am Composite. :( ")



for i in range(3, 101):
     check_if_prime(i)

check_if_prime(13577)