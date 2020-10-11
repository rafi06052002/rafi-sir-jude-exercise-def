# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 09:21:38 2020

@author: A.Rafi Muzakki
"""
#numero un0(1)
hours=0
minutes=0
seconds=0
   
def convert_to_days():
    global hours
    global minutes
    global seconds
    hours=int(input('Enter number of hours:'))
    minutes=int(input('Enter number of minutes:'))
    seconds=int(input('Enter number of seconds:'))
    return get_days(hours,minutes,seconds)
      
def get_days(hours,minutes,seconds):
    number_of_days=float((hours/24)+(minutes/1440)+(seconds/86400))
    print('The number of day is:',round(number_of_days,4))

convert_to_days()

#nomber2
def calc_weight_on_planet(weight_on_earth,surface_gravity=23.1):
    mass=(weight_on_earth/9.8)*surface_gravity
    print(mass)
    return mass
    
calc_weight_on_planet(120,9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120,23.1)

#nomber3
def num_atoms(amount_of_element,weight_of_element=196.97):
    avogadro_number=6.022*10**23
    number_of_atoms=(avogadro_number*amount_of_element)/weight_of_element
    print(number_of_atoms)
    return number_of_atoms  
 
 
num_atoms(10)
num_atoms(10,12.001)
num_atoms(10,1.008)
    
#nomber4
width=0
height=0
desired_width=0

def calc_new_height():
    global width
    global height
    global desired_width
    
   
    width=int(input('Enter the current width:'))
    height=int(input('Enter the current height:'))
    desired_width=int(input('Enter the desired width:'))
    
    
    return the_new_height(width,height,desired_width)
    
   
def the_new_height(width,height,desired_width):
    The_corresponding=float((desired_width/width)*height)
    print('The corresponding height is:',(The_corresponding))
    
calc_new_height()

#nomber5
fahrenheit=0
kelvin=0
celsius=0 
def convert_temp():
    global fahrenheit
    fahrenheit=int(input('Enter a temperature in Fahrenheit:'))
    print('The temperature in Celsius:',convert_to_celsius(fahrenheit))
    print('The temperature in Kelvin:',convert_to_kelvin(celsius))
    
    
def convert_to_celsius(fahrenheit):
     global celsius
     celsius=5/9*(fahrenheit-32)
     return celsius
     
    
    
def convert_to_kelvin(celsius):
    global kelvin
    kelvin=celsius+273.15
    return kelvin
    
convert_temp()
    
    
   
 


    
    
             
    
    
    


 

