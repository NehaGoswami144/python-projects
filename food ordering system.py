#!/usr/bin/env python
# coding: utf-8

# # HUNGRY!!!!!

# In[ ]:


MENU=input("\n1:pizza \n2:Burger \n3:drinks \n")
if MENU=="pizza"or MENU=="Burger"or MENU=="drinks":
    if MENU=="pizza":
        toppings =input("mushroom,paneer,capsicum")
        if toppings == "paneer":
            print ("your bill is 180:")
        elif toppings=="mushroom":
            print ("your ill is 150:")
        elif toppings=="capsicum":
            print("your bill is 160:")
        else :
            print("spcl pizza bill=200:")
            
    elif MENU=="burger":
        filling=input("\n1:cheese single \n2:cheese double \n3:makhani,\n4:noodles \n")
        if filling=="cheese single":
            print("your bill is 180:")
        elif filling=="cheese double":
            print("your bill is 220:")
        elif filling=="makhani":
            print("your bill is 280:")
        elif fillings =="noodles":
            print("your bill is 150:")
        else:
            print("special burger costs=350:")
            
    
           
    elif MENU=="drinks":
        drinks=input("\n1:soft_drinks \n2:shakes \n")
        if drinks=="soft_drinks":
            soft_drinks=input("\n1:coke \n2:pepsi \n3:fanta \n4:frooti \n")
            if soft_drinks=="coke":
                print("your bill is 40:")
            elif soft_drinks=="pepsi":
                print("your bill is 50:")
            elif soft_drinks=="fanta":
                print("your bill is 60:")
            elif soft_drinks=="frooti":
                print("your bill is 70:")
            else:
                print("go for other options:")
        elif drinks=="shakes":
            shakes=input("\n1:kit-kat \n2:oreo \n3:chocolate \n4:black-current \n")
            if shakes=="kit-kat":
                print("your bill is 270:")
            elif shakes=="oreo":
                print("your bill is 380:")
            elif shakes=="chocolate":
                print("your bill is 260")
            elif shakes=="black-current":
                print("your bill is 240")
            else:
                print("go for other options:") 
        else:
            print("we have only these options:")
            
    
else:
    print("not availbl:")

