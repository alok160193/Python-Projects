# *******************************|PROJECT- ADVANCE CALCULATOR|***********************************************
# To find 
# factorial,Table of any no. , sum of given natural nos., fabonacci series, check prime,to find factors, square root, cube root etc.


class Advance_Calculator:
    def __init__(self):

        print("*************Welcome to Advance Calculator****************")

    def factorial(self, n1):

        p = 1
        for i in range(n1):
            p = p * (n1 - i)
        print(p)

    def table(self,n2):
        for i in range(1, 11):
            print(f"{n2}X{i}={n2*i}")

    def sum_of_first_n_natural_numbers(self, n3):
        s = 0
        for i in range(1, n3 + 1):
            s = s + i
        print(f"Sum of n natural numbers is {s}")
    
    def fabonaci_series(self,nterms):
        n1,n2=0,1
        nth=0
        count=0
        
        if nterms<=0:
            print("pls enter positive integer")
        elif nterms==1:
            print(n1)
        elif nterms>1:
            print("Fabonacci Series:")
            while(count< nterms):
                print(n1)
                nth=n1+n2
                n1=n2   #updating values
                n2=nth  #updating values
                count+=1
    def check_prime(self,n5):
        if n5>1:  # 1 is not a prime no.
            for i in range(2,n5):             # Using for with else clause 
                if n5%i==0:
                    print(f"{n5} is not a prime no.")
                    break
            else:
                print(f"{n5} is a prime no.")
                    
        else:
            print(f"{n5} is not a prime no.")

    def find_factors(self,n6):
        print(f"factors of {n6} are:\n" )
        for i in range(1,n6+1):
            while n6%i==0:
                print(f"{i}\n")
    def find_sqrt(self,n7):
        print(f"Square Root of {n7} is:{n7**0.5}\n" )
    def find_cubert(self,n8):
        print(f"Cube Root of {n8} is:{n8**(1/3)}\n" )
                
           
        
            

        
        
ob = Advance_Calculator()
c = input('''Enter your choice
Factorial-1
Table-2
Sum of first n Natural numbers-3
Fabonacci series upto n given terms-4
To Check Prime or not-5
To find factors of a given no.-6
To find Square root of a given no.-7
To find Cube root of a given no.-8\n''')

if c == "1":

    n1 = int(input("enter a no. to find its factorial "))
    # if isinstance(n1, int)==True:
    ob.factorial(n1)
    # else:
    #     print("plz enter in integer value")
elif c == "2":
    n2 = int(input("enter a no. to print its table "))
    ob.table(n2)
elif c == "3":
    n3 = int(
    input("enter a no. till which you wanna find sum of natural numbers "))
    ob.sum_of_first_n_natural_numbers(n3)
elif c == "4":
    nterms = int(input("enter nth term till u wanna see fabonnaci sequence\n"))
    ob.fabonaci_series(nterms)
elif c == "5":
    n5 = int(input("enter a no. to check whether it is prime or not\n"))
    ob.check_prime(n5)
elif c == "6":
    n6 = int(input("enter a no. to find it's factors\n"))
    ob.find_factors(n6)
elif c == "7":
    n7 = int(input("enter a no. to find it's square root\n"))
    ob.find_sqrt(n7)
elif c == "8":
    n8 = int(input("enter a no. to find it's cube root\n"))
    ob.find_cubert(n8)
else:
    print('''Wrong Choice !\nPlease select from choices given above in numeric form''')
