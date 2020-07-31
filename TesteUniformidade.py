# -*- coding: utf-8 -*-
"""
@author: Pedro Brandalise
"""

import math

class TesteUniformidade:

    def __init__(self, fileName, numberOfIntevals):
        self.__fileName = fileName
        self.__samples = [] 
        self.__numberOfIntervals = numberOfIntevals
        

        self.__step = 1/numberOfIntevals
        
        self.__fo = [] #frequencia observada
        for i in range (numberOfIntevals):
           
            self.__fo.append(0)
        
        self.__numberOfSamples = 0
        
        self.fe = 0 #fequencia esperada

        self.__pi = []

        self.__gx = []
        self.__fx = []

        self.__uniformityTestKs()




    def __uniformityTestKs(self):

        self.__readFile(self.__fileName)
        self.__samples.sort()

        for i in range(0, len( self.__samples)):
            
            for j in self.__fo:
                
                if (self.__samples[ i ] >= (j * self.__step)  and self.__samples[ i ] < (j*self.__step + self.__step)):
                    self.__fo[j] += 1
                    break
        
        for i in range(0, self.__numberOfIntervals):
    
            self.__pi.append( self.__fo[i]/ self.__numberOfSamples)

        self.__gx.append(self.__pi[0])
        for i in range(1, self.__numberOfIntervals):
            self.__gx.append( self.__pi[i] +self.__gx[i-1])

        self.__fx.append(self.__step)
        for i in range(1, self.__numberOfIntervals):
            self.__fx.append(self.__step + self.__fx[i-1])

        ksCalc = 0

        for i in range(0,self.__numberOfIntervals):
            if abs( self.__fx[i] - self.__gx[i] )  > ksCalc:
                ksCalc = abs( self.__fx[i] - self.__gx[i] )

        ks5 = 1.36/math.sqrt(self.__numberOfSamples)


        print ("TESTE DE UNIFORMIDADE PARA "+ self.__fileName)
        print ( 'K-S calculado: '+ str(ksCalc))
        print ('K-S 5%: '+ str(ks5))

        if ksCalc<ks5:
            print ('Aceita H0')
        else:
            print ('rejeita H0')



    def __readFile(self, filename):
        try:
            myFile = open(filename, "r")
            """
            Faz a leitura linha por linha e adiciona à lista como string
            evitando adição de espaço em branco
            """
            for y in myFile.read().split('\n'):
                if y:
                    self.__samples.append(float(y))
                    
            myFile.close()

        except:
            raise Exception("Could´t open the file")
        self.__numberOfSamples = len(self.__samples )

    