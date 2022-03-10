#!/usr/bin/env python
# coding: utf-8

# # Q1. Write a program to accept percentage from the user and display the grade according to the following criteria:
# 
#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                               B
#          >= 60 and <= 80                              C
#          below 60                                     D

# In[ ]:


your_percentage=int(input('enter ur percentage'))
if your_percentage>90:
    print('Grade is A')
elif your_percentage>80 and your_percentage<=90:
    print('Grade is B')
elif your_percentage>=60 and your_percentage<=80:
    print('Grade is C')
else:
    print('Grade is D')
    
    


# # Q2. Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :
#     
#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                                     10%
#         <= 50000                                                  5%
# 

# In[ ]:


cost_price=int(input('price'))
if cost_price>100000:
    print('tax is',(15/100)*cost_price)
elif cost_price>50000 and cost_price<=100000:
    print('tax is',(10/100)*cost_price)
else:
    print('tax is',(5/100)*cost_price)


# # Q3. Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.

# In[ ]:


number=int(input(' enter any num between 1 to 7 \n'))
if number==1:
    print('sunday')
elif number==2:
    print('monday')
elif number==3:
    print('tuesday')
elif number==4:
    print('thrusday')
elif number==5:
    print('friday')
elif number==6:
    print('satday')
else:
     print('please enter the number between 1 to 7')


# # Q4. Write a program to check whether an year is leap year or not.

# In[ ]:


year=int(input('year'))
if year%4==0:
    print('leap year')
elif year%400==0:
    print('leapuu')
    
else:
    print('not leap year')
    


# # Q5 : write a programme reversing the number input by user.

# In[1]:


num=input('h')
n=list(num)
n[::-1]



# # Q6: Write a programme to convert the temperature enttered by user and also tell which conversion they required (celsius to 

# In[ ]:



conv=input('f or c')
tempr=int(input('tempature'))
if conv=='f'and conv=='F':
    fh= (tempr*1.8)+32
    print('ur temp in celsius is',fh)
elif conv=='c' and conv=='C':
    cl= (tempr - 32) / 1.8
    print('ur temp in calsius is ',cl)


# # Q7. Write a program to check whether a number is even or odd.

# In[ ]:


numer=int(input('enter ur num'))
if numer%2==0:
    print('the number is even')
else:
    print('the numb is odd')
    
    
    


# # Q8. Accept the electric units from user and calculate the bill according to the following rates.
# 
# First 100 Units     :  Free
# 
# Next 200 Units      :  Rs 2 per day.
# 
# Above 300 Units    :  Rs 5 per day.
# 
# if number of unit is 500 then total bill = 0 +400 + 1000 = 1400

# In[ ]:


unit = int(input("Enter number of units"))

if ut <=100:

     amt = 0

elif ut >100 and ut <= 300:

     amt = (ut-100)*2

else:

     amt = 400 + (ut - 300)*5

print("Total amount to pay is ", amt)


# # Q9. Write a program to display the last digit of a number.
# 
# 

# In[43]:


numbr=int(input('enter ur um'))
answr=numbr%10
print(answr)


# # Q10. Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not.

# In[47]:


numbr=int(input('enter ur um'))
answr=numbr%10
if answr%3==0:
    print('tis is divisible of 3')
else:
    print('ths is not')


# # Q11. write a function to count the no. of elements in a list .and if the count of element is greater than 6 check print the element and say lengthy .

# In[ ]:


numbr=int(input('enter ur number:\n'))
list(numbr)
if len(numbr)>6:
    print('it is lengthy')
else:
    print('it is not')


# # Q12. Write a program to check whether a number (accepted from user) is positive or negative.

# In[55]:


numbr=int(input('enter ur um'))
if numbr>0:
    print('it is positive')
else:
    print('it is negatv')


# # Q13 :write a programme to check whether the chracter enterred by user contains vowels or not

# In[ ]:


chra=input('charctr')
vow='aeiouAEIOU'
if chra in vow:
    print('it contains vowel')
else:
    print('it is not')


# # Q14. Accept the marked price from the user and  calculate the Net amount as(Marked Price –    Discount) to pay according to following criteria:
# 
# #Marked Price   |  Discount
# >10000	    |  20%
# 
# >7000 and <=10000   |	15%
# 
# <=7000	            | 10%

# In[ ]:


mp=int(input('mp'))
if mp>10000:
    disc=mp*0.5
    namt=mp-disc
    print('net amount is',namt)
elif mp>7000 and mp<=10000:
    disc=mp*15/100
    namt=mp-disc
    print('net amount is',namt)
elif mp<=7000:
    disc=mp*0.1
    namt=mp-disc
    print('net amount is',namt)


# # Q15. Write a program to accept two numbers and mathematical operators and perform operation accordingly.

# In[ ]:


enter1=int(input('numbeer'))
enter2=int(input('number'))
oper=input('which mathicl op u wnt to prfrm')
if oper=='+':
                 ans=enter1+enter2
                 print('ans is',ans)
if oper=='-':
                 ans=enter1-enter2
                 print('ans is',ans)
if oper=='*':
                 ans=enter1*enter2
                 print('ans is',ans)
if oper=='/':
                 ans=enter1/enter2
                 print('ans is',ans)

                 
                 
                 
                 


# # Q16: write a function to print the table in the range 3 to 8 and print the table in reverse order.

# In[ ]:


for i in range(3,9):
   
    for j in range(10,0,-1):
        print(i,"x",j,"=",i*j)
    print('///////')


# # Q17: Given an integer, n, perform the following conditional actions:
# If  n is odd, print Weird.
# If  n is even and in the inclusive range of  2 to 5, print Not Weird.
# If  n is even and in the inclusive range of  6 to 20, print Weird.
# If  n is even and greater than  20 , print Not Weird

# In[ ]:


n=int(input('enter any number'))
if n%2!=0:
    print('weird')
if n%2==0 and n>20:
    print ('not weird')
    if n%2==0 and n==range(2,5):
        print('not weird')
    elif n%2==0 and n==range(6,20):
        print('weird')


# # Q18. Write a function to compute the population of india in 2050 when i say it will be 7 times of todays population.

# In[ ]:


def population():
    population2021=1.36
    population2050=(population2021*7)
    print(population2050)
population()


# # Q19.Write a program to take toss as input from the user and if heads comes india wins the toss and take input from india what it decides to do bat or bowl.
# #If india choose to bat first they have to score more than 300 runs in 40 overs . if they fail to achieve this they should #score 330 in 50 overs .
# #If india chooses to bowl they have to all out the opposition within 280 runs else . the runrate should not be greater than 5 #for fifty overs. 
# #If india loses the toss they have to chase max of 300 runs above which they need to change the batting order and sent pandeya for slogging.
# 

# In[ ]:


toss=input('\n1:head \n2:tale:\n')
if toss=="head":
    india=input('bat or bowl')
    if india=='bat':
        run=int(input('run in batting'))
        overs=int(input('overs'))
        if run>300 and overs<=40:
            print('indiaaa')
        elif run>=330 and overs<=50:
            print('indiaaa')
        else:
            print("india lost it")
    elif india=='bowl':
        oppo_run=int(input('oppo run'))
        runrate= int(input('runrate'))
        overs= int(input('overs in bowling'))
        if oppo_run==range(280) and runrate<5 and overs ==50:
            print('indiaaaa')
        else:
            print('india lost it')
    

elif  toss=="tale":
    run=int(input('run loosers'))
    if run>=300:
        print('go on')
    else:
        print('send pandaya for slogging')
        


# # Q20. A company decided to give bonus to employee according to following criteria:
# 
#     Time period of Service                Bonus
# 
#     More than 10 years             10%
# 
#     >=6 and <=10                   8%
# 
#     Less than 6 years              5%
# 
#     Ask user for their salary and years of service and print the net bonus amount.

# In[ ]:


service =int(input("Enter the time period of service"))
salary =int(input("Enter your salary"))
if service > 10:
     b=10/100*salary
if service >=6 and service <=10:
     b = 8/100*salary
if service < 6:
    b = 5/100*salary
print("Bonus is ", b)

