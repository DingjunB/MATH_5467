# Uncomment this to see the pre-exercise problems:
############################################################################## 
#### Variables
###Numerics:
##a = 2
##b = 4
##print(a + b) # 6
##print(a * b) # 8
##
###Strings:
##a = 'hello'
##b = ' '
##c = 'world'
##print(a + b + c) #'hello world'
##print(5 * a) #'hellohellohellohellohello'
##
###Lists:
##a = [4, 'hello world', 3.141259]
##b = ['data science', 46]
##print(a + b) # [4, 'hello world', 3.141259, 'data science', 46]
##print(3 * b) # ['data science', 46, 'data science', 46, 'data science', 46]
##
###For loop:
##for i in range(10):
##    print(i)
##print('done')
##
##
###Fix it: (indentation not correct)
##for i in range(10):
##    j = 2*i
##    print(j)
##print('fixed')
##
###While loop:
##i = 0
##while i < 10:
##    print(i)
##    i += 1
##
###If statements:
##n = 41
##print('n is equal to', n)
##if n > 50:
##    print('n is larger than 50')
##else:
##    print('n is less than or equal to 50')
##
###longer if else statements:
##if n > 50:
##    print('n is larget than 50')
##elif n > 40:
##    print('n is larger than 40 but less than or equal to 50')
##else:
##    print('n is smaller or equal to 40')
###############################################################################
#Exercises:
#1.
def Taylor_approximate_sine(x):
    approx = x - x**3/(3*2) + x**5/(5*4*3*2) + x**7/(7*6*5*4*3*2)
    return approx

#2.
def Babylonian_method_for_sqrt_x(x, tol = 1e-5):
    if x < 0:
        print('x is smaller than 0.')
    else:
        sqrt_x = x
        while abs((sqrt_x)**2 - x) > tol:
            sqrt_x = (1/2)*(sqrt_x + x/sqrt_x)
        return sqrt_x

#3.
# On Overleaf

#4. 
def Sieve_of_Era(n):
    list_of_number = list(range(2, n + 1))
    list_to_exclude = []
    list_of_prime = []
    for i in range(len(list_of_number)):
        j = 2
        while list_of_number[i] * j <= n:
            exclude = list_of_number[i] * j
            if exclude not in list_to_exclude:
                list_to_exclude.append(exclude)
            j +=1
    list_of_prime = list(set(list_of_number) - set(list_to_exclude))
    list_of_prime.sort()
    return(list_of_prime)


### Failed Attempt for Question 4:
##    list_to_exclude = []
##    list_of_number = list(range(2, limit + 1))
##    temp = list(range(2, limit + 1))
##    print('temp:', temp)
##    for j in range(len(temp)):
##        print(len(temp))
##        prime = temp[j]
##        for i in range((limit % prime) + 1):
##            exclude = prime**i
##            list_to_exclude.append(exclude)
##            if exclude in temp:
##                temp.remove(exclude)
##                print('update temp:',temp)
##    print(list_to_exclude)
##    list_of_prime = list(set(list_of_number) - set(list_to_exclude))
##    return (list_of_prime)
