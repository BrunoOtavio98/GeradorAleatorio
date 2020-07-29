# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 15:16:32 2020

@author: Will
"""
import math

class TesteIntervalo:
    
    def __init__(self, fileName, digit):
        self.__fileName = fileName
        self.__digit = str(digit)
        self.__intervalCounter = 0
        self.__samples = [] #String
        self.__allIntervals = [] #int
        self.__intervals = [] #int
        self.__freq = [] #int
        self.__pi = [] #float
        self.__GX = [] #float
        self.__pk = [] #float
        self.__FX = [] #float
        self.__FX_GX = [] #float
        self.__ksCalc = 0
        self.__ks5perCent = 0
        self.__intervalTestKS()

    """
    Faz o teste do intervalo utilizando
    """
    def __intervalTestKS(self):
        self.__readFile(self.__fileName)
        
        #Executa a contagem dos intervalos e guarda em __allIntervals
        for sample in self.__samples:
            if(sample[2] == self.__digit):
                self.__allIntervals.append(self.__intervalCounter)
                self.__intervalCounter = 0
            else:
                self.__intervalCounter += 1
        
        """
        Teste Kolmogorov-Smirnov
        """
        #Separa todos os intervalos apenas em numeros nao repetidos
        for i in range(min(self.__allIntervals, key=int),  max(self.__allIntervals, key=int)):
            self.__intervals.append(i)
                    
        #Calcula a frequencia de cada intervalo
        #Calcula a probabilidade de se obter um intervalo de comprimento K
        for interval in self.__intervals:
            self.__freq.append( self.__allIntervals.count(interval) ) 
            self.__pk.append(0.9 ** interval * 0.1)
        
        #Calcula a probabilidade de cada frequencia
        for n_intervals in self.__freq:
            self.__pi.append(n_intervals / sum(self.__freq))
        
        #Somatorio da probabilidade das freq G(X)
        #Somatorio da probabilidade de se obter um intervalo de comprimento K G(X)
        #Calcula o valor absoluto da diferença entre F(X) e G(X)
        self.__GX.append(self.__pi[0])
        self.__FX.append(self.__pk[0])
        for i in range(1, len(self.__pi)):
            self.__GX.append(self.__GX[i-1] + self.__pi[i])
            self.__FX.append(self.__FX[i-1] + self.__pk[i])
            self.__FX_GX.append(abs(self.__FX[i-1] - self.__GX[i-1]))
      
        #K-S calculado
        #K-S 5%
        self.__ksCalc =  max(self.__FX_GX )
        self.__ks5perCent = 1.36 / math.sqrt(sum(self.__freq)) 
        
        #Imprime os resultados...
        print("Para D => " + self.__digit + " do conjunto de dados do arquivo " + self.__fileName)
        print("K-S(Calc.) => " + str(self.__ksCalc))
        print("K-S(5%) => " + str(self.__ks5perCent))
        
        if(self.__ksCalc < self.__ks5perCent):
            print("Como K-S(Calc.) < K-S(5%) => Aceita H0 \n")
        else:
            print("Como K-S(Calc.) > K-S(5%) => Rejeita H0 \n")
            

    """
    Faz a leitura do arquivo para uma list
    """
    def __readFile(self, filename):
        try:
            myFile = open(filename, "r")
            """
            Faz a leitura linha por linha e adiciona à lista como string
            evitando adição de espaço em branco
            """
            for y in myFile.read().split('\n'):
                if y:
                    self.__samples.append(y)
                    
            myFile.close()
        except:
            raise Exception("Could´t open the file")
            
        