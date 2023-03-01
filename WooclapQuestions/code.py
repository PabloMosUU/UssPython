#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 11:03:33 2022

@author: alpiz001


"""
#%% Wooclap lecture 4
print("Hello World!")

print("greet the Dutch") 
print("Hello Netherlands!")

#print("greet the Dutch") 
print("Hello Netherlands!")


a = 5
b = 8
c = a
a = b
b = c
print(f"a={a} and b={b}") 

a = 5
b= 8
c = a
a = b
b= c
print("a={0} and b={1}".format(a, b)) 

print(a, "+", b, "is", a+b) 


#alice, bob, and charlie are friends 
#thy decide to party.
#Follow their journey...
 
alice_can_drink = True
bob_can_drink = False
charlie_can_drink = True

alice_has_money = False
bob_has_money = True
charlie_has_money = True

alice_buys_alcohol = alice_can_drink and alice_has_money
bob_buys_alcohol = bob_can_drink and bob_has_money
charlie_buys_alcohol = charlie_can_drink and charlie_has_money

alice_can_party = alice_buys_alcohol or ((not alice_buys_alcohol) and (bob_buys_alcohol or charlie_buys_alcohol))


    
#%% wooclap lecture 6

# base = x
# exponent = n
def pow(base, exponent):
  # Base Case
  if exponent == 0 :
    return 1
    
  # Recursive Case
  else :
    return base * pow(base, exponent - 1);

def sum(n):
    #base case
    if n == 1:
        return 1
    
    #recursive case
    else:
        return n + sum(n-1)
#%% start 
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

#%% functions and scope 

x = 300

def func1():
  x = 200
  print(x)

def func2():
  global x
  print (__name__)
  x = 400
  
func1()
print(x)
func2()
print(x)

#%%
print (__name__)
#if __name__ == "__main__":
