#Take the Numbers in list
numbers=(1,2,3,4,5,6,7,8,9)
count_1=0 #counter for even numbers
count_2=0 #counter for odd numbers
# we know if no. is divisible by 2 then it is even nunbers 
#and if not divisible ny 2 then it is odd numbers
for no in numbers:
    if no%2==0:
        count_1+=1
    else :
        count_2+=1

print("number of even numbers:",count_1)
print("number of odd numbers:",count_2)