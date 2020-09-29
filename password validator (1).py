#!/usr/bin/env python
# coding: utf-8

# In[ ]:


password = input("Password: ")



password_list = list(password)

password_len = len(password_list)

spaces = " " in password

number = any(x.isdigit() for x in password)

special = any(x.isalnum() for x in password)

if spaces == False and number == True and special == True and 5 <= password_len <= 10:
    print("valid password")
else:
    print("not valid password")

