# -*- coding: utf-8 -*-
import time


class GeradorLinear:
	
    __self_seed = 0     

    def __init__(self, a, m, c):
        self.__a = a
        self.__m = m
        self.__c = c
        self.__seed = __self_seed 
        self.__total_time = 0.0                       
    
    def __init__(self, a, m, c, seed):
        self.__a = a
        self.__m = m
        self.__c = c
        self.__seed = seed
        self.__total_time = 0.0
        
    def rand(self, quantity, file_name):
        __i = 0
        __temp = 0
        __last_numbers = []                       
        __integer = []
        
        __t1 = time.time()
       
        __integer.append(self.__seed)
        
        for __i in range(1, quantity):
            __integer.append( self.__MOD( __integer[__i - 1] * self.__a  + self.__c, self.__m ) ) 
            __last_numbers.append(  __integer[ __i ] / self.__m  )

        __t2 = time.time()
       
        self.__total_time = __t2 - __t1

        self.__save_data(__last_numbers, file_name)

        return __last_numbers

    def getTotalTime(self):
        return self.__total_time

    def __MOD(self , number, divisor):
        return number % divisor
            
    def __save_data(self, numbers, file_name):
        
        try:
            myFile = open(file_name + ".TXT", "w+")
            for n in numbers:
                myFile.write(str(n) + "\n")

        except:
            raise Exception("Could not open the file")
        finally:
            myFile.close()






