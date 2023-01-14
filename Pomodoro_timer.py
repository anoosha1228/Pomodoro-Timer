#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import winsound

setTotalpom = int(input("Enter total number of Pomodoro : "))

setTime = int(input("Enter Pomodoro time in minutes : "))

breakTime = int(input("Enter break time in minutes : "))

longTime = int(input("Enter long break time in minutes : "))

Totalbreak = setTotalpom-1

print("Your Pomodoro Time starts now !")
while setTotalpom>0:
  Insec = setTime*60
  breakInsec = breakTime*60
  longInsec = longTime*60
  
  while Insec:
    min = Insec//60
    sec = Insec%60
    timer = '{:02d}:{:02d}'.format(min,sec)
    print('\r',timer, end='')
    time.sleep(1)
    Insec-=1
  
  if Totalbreak>0:
    print("\nShort break started")
    while breakInsec>0:
      breakmin = breakInsec//60
      breaksec = breakInsec%60
      timer = '{:02d}:{:02d}'.format(breakmin,breaksec)
      print('\r',timer, end='')
      time.sleep(1)
      breakInsec-=1
    Totalbreak-=1
    print("\nBack to study")
  else:
    print("\nLong break started")
    while longInsec:
      longmin = longInsec//60
      longsec = longInsec%60
      timer = '{:02d}:{:02d}'.format(longmin,longsec)
      print('\r',timer, end='')
      time.sleep(1)
      longInsec-=1
    print("\n\nHurray you have succesfully completed your study time !")
  setTotalpom-=1
  


# In[ ]:




