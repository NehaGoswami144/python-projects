#!/usr/bin/env python
# coding: utf-8

# # DISCOUNT OFFERS

# In[3]:


def sale():
    big_sales=input("\n1:electronics \n2:appreals \n3:baby prducts \n4:personal care \n")
    if big_sales=="electronics": 
        electronics=input("\n1:phone \n2:laptop \n3:ac and refrigerator \n")
        if electronics=="phone":
            print("ur discount is 10%:")
        elif electronics=="laptop":
            print("ur discount is 5%:")
        elif electronics=='ac and refrigerator':
            print("ur discount is 20%:")
        else:
            print("no offer:")
            
    elif big_sales=="appreals":
        appreals=input("\n1:male \n2:female \n")
        if appreals=="male":
            print("no offer:")
        elif appreals=="female":
            female=input("\n1:proffesional \n2:personal")
            if female=="proffesional":
                print("ur discount is 30%:")
            elif female=="personal":
                print("ur discount is 20%:")
            else:
                print("oops!! mam u missed it")
        else :
            print("sorry we have only these options")
    elif big_sales=="baby":
        print("your dscount is 40%:")
    elif big_sales=="personal care":
        print("shop above 600$ discount'll be 50%:")
    else :
        print("we have specific item's offer")
sale()

