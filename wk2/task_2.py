"""
Write a program that:
1. Takes two positive integers as input (range start and end)
2. Validates the input (must be positive integers)
3. Finds all prime numbers within the given range (inclusive)
4. Displays the primes in a formatted output (10 numbers per line)
5. Handles invalid inputs gracefully
"""

# checking for prime or not 

def prime(a):
 if a<=1: # prime should be more than 1 
     return False
 for i in range(2, int(a**0.5)+1): # checking prime or not by using square root 
    if a%i==0: # if it is divisible then not a prime
        return False
     
 return True # we cant use else if we use it w1ont check for othr number divisibility
       
       

while True: #
        try:
          Start=int(input("enter the start number\n")) # asking user to enter start and end values 
          End=int(input("enter the end number\n"))

          if Start<= 0 or End <=0: # those values shouln't be negative range
               print(" numbers are no longer positive range")
               continue
          if Start>End: # checking start is smaller compared to end 
               print("Enter greater number for End than Start")
               continue
          
          print("prime numbers are : ")
         
          found = False # created flg toknow about divisible or not
          col=0 # to new line creatin after 5 entries 
          for n in range(Start, End + 1): # going along woth for loop within range including both start and end values
              if prime(n):
                  print(f"{n:5}", end=" ") # printing prime number with :5 means to tell 5 conts and separated by space 
                  found = True # if foud flag trues number falls under prime
                  col+=1  # counting to fill upto 5 
                  
                  if col%5==0: # once counting gets 5 then it will look for nect line
                      print()
 

          if not found: # if found flag is 0 means no  primes are between that range 
             print("NO prime values between this range")

          break # after successfull executuon , loo will gwt stop executing

         

        except ValueError: # it will handle error id entr wrong values 
          print("check the values you have entered")