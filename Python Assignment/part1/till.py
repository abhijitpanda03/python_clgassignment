# Write a python program to find following using looping and decision making without function
print("0: To exit out of the program")
print("1: Sum of all digits of any numbers")
print("2: Sum of all even digits of any numbers")
print("3: Sum of all odd digits of any numbers")
print("4: Sum of all prime digits")
print("5: Difference between average of all even digits except divisible by 4 and avearge of all odd digits except divisble by 3")
print("6: Find kth digit from frontside or back side of any digits number and find its poistional value")
print("7: Sum of product of consecutive digits of any digit number")
print("8: Sum of product of consecutive even digits of any digit number")
print("9: Sum of product of consecutive odd digits of any digit number")
print("10: Sum of product of consecutive prime digits of any digit number")
print("11: Difference between Sum of product of consecutive even digits except 2 and 6 and Sum of product of consecutive odd digits except 3 and 7 of any digit number")


while True:
    choice=int(input("\nEnter your choice:"))
    if choice<=11:
        sums=0
        if choice ==1:
            count=int(input("How many numbers ? "))
            for i in range(count):
                num=int(input())
                sums+=num
            print("Sum of all numbers:",sums)

        elif choice==2:
            count=int(input("How many numbers ? "))
            num=(count*2)+1
            for i in range(num):
                if i%2 ==0:
                    sums+=i
            print("Sum of even numbers:",sums)
        
        elif choice==3:
            count=int(input("How many numbers ? "))
            num=(count*2)+1
            for i in range(num):
                if i%2 !=0:
                    sums+=i
            print("Sum of odd numbers:",sums)
        
        elif choice==4:
            count=int(input("How many numbers ? "))
            sums=2
            for i in range(2,count+1):
                num=2
                for num in range(2,i):
                    if int(i%num)==0:
                        num=i
                        break
                if num is not i:
                    sums+=i
            print("Sum of prime number:",sums)
        
        elif choice==5:
            num=input("Enter a number:")
            evens=[]
            odds=[]
            for i in num:
                i=int(i)
                if i% 2 ==0 and i% 4 != 0:
                    evens.append(i)
                elif i% 2 != 0 and i%3 != 0:
                    odds.append(i)
            diff=sum(evens)/len(evens) - sum(odds)/len(odds)
            print("Difference between average:",diff)
        
        elif choice==6:
            num = input("Enter a number:")
            k = int(input("Enter K: "))
            if k<len(num):
                print("\nFront:",num[k-1],"\nBack:",num[-k])
            else:
                print("\n Invalid K")
        
        elif choice==7:
            num = input("Enter a number:")
            for i in range(0,len(num)-1):
                sums+=(int(num[i]) * int(num[i+1]))
            print("Sum of product of consecutive digits:",sums)
        
        elif choice==8:
            num = input("Enter a number:")
            arr=[]
            for i in range(0,len(num)):
                if int(num[i])%2 ==0:
                    arr.append(num[i])
            for i in range(0,len(arr)-1):
                sums+=(int(arr[i]) * int(arr[i+1]))
            print("Sum of product of consecutive even digits:",sums)
        
        elif choice==9:
            num = input("Enter a number:")
            arr=[]
            for i in range(0,len(num)):
                if int(num[i])%2 !=0:
                    arr.append(num[i])
            for i in range(0,len(arr)-1):
                sums+=(int(arr[i]) * int(arr[i+1]))
            print("Sum of product of consecutive odd digits:",sums)

        elif choice==10:
            num = input("Enter a number:")
            prime=['2','3','5','7']
            digits=[]
            for i in num:
                if i in prime:
                    digits.append(i)
            for x in range(0,len(digits)-1):
                sums+=int(digits[x])*int(digits[x+1])
            print("Sum of product of consecutive prime digits:",sums)
        
        elif choice==11:
            num=input("Enter a number:")
            num.strip()
            even=[ int(i) for i in num if int(i) in [0,4,8]]
            odd=[ int(i) for i in num if int(i) in [1,5,9]]
            sum_even=sum([even[i]*even[i+1] for i in range(0,len(even)-1)])
            sum_odd=sum([odd[i]*odd[i+1] for i in range(0,len(odd)-1)])
            diff=sum_even-sum_odd
            print("Difference:",diff)
        
        elif choice==0:
            break
    else:
        print("You have entered a wrong choice, please enter a valid choice.")