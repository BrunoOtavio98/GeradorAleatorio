# -*- coding: utf-8 -*-
"""
@author: Pedro Brandalise
"""

import math

class TesteUniformidade:

    ''' fileName: nome do arquivo a ser analisado 
        numberOfIntervals: numero de intervalos que sera usado pelo teste de uniformidade
        graph: valor booleano que indica se o grafico de probabilidade em cada intervalo será mostrado
    '''
    def __init__(self, fileName, numberOfIntevals, graph):
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

        self.__graph= graph
        self.__uniformityTestKs()




    def __uniformityTestKs(self):
         
        self.__readFile(self.__fileName)
        # acontece a ordenação para facilitar a contagem de valor em cada intervalo
        self.__samples.sort()

        # conta quantos valores tem para cada intervalo
        for i in range(0, len( self.__samples)):
            
            for j in range(0, len(self.__fo)):
                
                if (self.__samples[ i ] >= (j * self.__step)  and self.__samples[ i ] < (j*self.__step + self.__step)):
                    self.__fo[j] += 1
                    break

        #calcula as probabilidades para cada intervalo
        
        for i in range(0, self.__numberOfIntervals):
    
            self.__pi.append( self.__fo[i]/ self.__numberOfSamples)
        
        # exibe o grafico caso seja solicitado
        if self.__graph:
            self.__graphPlot()


        # calcula G(x)
        self.__gx.append(self.__pi[0])
        for i in range(1, self.__numberOfIntervals):
            self.__gx.append( self.__pi[i] +self.__gx[i-1])


        #calcula F(x)
        self.__fx.append(self.__step)
        for i in range(1, self.__numberOfIntervals):
            self.__fx.append(self.__step + self.__fx[i-1])


        #calculo do K-S calculado
        ksCalc = 0

        for i in range(0,self.__numberOfIntervals):
            if abs( self.__fx[i] - self.__gx[i] )  > ksCalc:
                ksCalc = abs( self.__fx[i] - self.__gx[i] )


        #calculo do K-S 5%
        ks5 = 1.36/math.sqrt(self.__numberOfSamples)
        

        print ("TESTE DE UNIFORMIDADE PARA "+ self.__fileName)
        print ( 'K-S calculado: '+ str(ksCalc))
        print ('K-S 5%: '+ str(ks5))

        if ksCalc<ks5:
            print ('Aceita H0')
        else:
            print ('rejeita H0')

    def __graphPlot(self):
        import matplotlib.pyplot as plt
        x= []
        x.append(0)
        for i in range(1, self.__numberOfIntervals):
            x.append(x[i-1] + self.__step)
        plt.plot( x, self.__pi )
        plt.ylabel("probabilidade de ocorrencia")
        plt.title(self.__fileName)
        
        plt.show()


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

    