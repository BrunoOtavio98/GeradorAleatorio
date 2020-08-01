#!/usr/bin/python
# -*- coding: utf-8 -*-

from math import sqrt
from os import path, mkdir

class TestePermutacoes:
    def __init__(self, file_name= ""):
        self.__file_name = file_name
        self.__output_folder = "permutacoes_result"

    def setFileName(self, file_name):
        self.__file_name = file_name

    def test(self):
        lines = self.readFileAsArray()
    
        if(not lines):
            print(print("Não foi possivel abrir o arquivo: " + self.__file_name))
            return lines
        
        total = len(lines) - 1
        
        Fo = self.permutate(lines)

        total = 0
        for f in Fo:
            total += f

        size = len(Fo)
        
        fg = [0, 0, 0, 0, 0, 0]
        pi = [0, 0, 0, 0, 0, 0]
        G = [0, 0, 0, 0, 0, 0]
        Fx = [0, 0, 0, 0, 0, 0]
        fx = 1/size

        for i in range(0, size):
            pi[i] = (Fo[i]/total)

        G[0] = pi[0] 
        for i in range(1, size):
            G[i] = G[i - 1] + pi[i]

        Fx[0] = fx
        print(fx)
        for i in range(1, size): 
            Fx[i] = Fx[i - 1] + fx

        for i in range(0, size):
            fg[i] = abs(Fx[i] - G[i]) 

        fg.sort()
        ks_calc = fg[size - 1]
        ks_5 = 1.36/sqrt(total)
        Ho = (ks_calc < ks_5)

        print("Ks_5: " + str(ks_5))
        print("Ks_calc: " + str(ks_calc))
        print("Ho: " + str(Ho))

        self.saveResult(Ho, Fo, pi, G, fx, Fx, fg)


    def saveResult(self, Ho, Fo, pi, G, fx, Fx, fg): 
        message = "Erro ao criar o arquivo"   
        try:
            if(not path.exists(self.__output_folder)):
                mkdir(self.__output_folder)

            myFile = open(path.join(self.__output_folder, self.__file_name + "_PERMUTACOES.TXT"), "w")
            myFile.write("Fo,")
            for f in Fo:
                myFile.write(str(f) + ",")

            myFile.write(" \n")

            myFile.write("pi,")
            for p in pi:
                myFile.write(str(p) + ",")
            
            myFile.write("\n")

            myFile.write("G,")
            for g in G:
                myFile.write(str(g) + ",")
                
            myFile.write("\n")

            myFile.write("Fx,")
            for f in Fx:
                myFile.write(str(f) + ",")
            myFile.write("\n")

            myFile.write("fx,")
            myFile.write(str(f) + ",")
            myFile.write("\n")

            myFile.write("fg,")
            for f in fg:
                myFile.write(str(f) + ",")
            myFile.write("\n")

            if(Ho):
                myFile.write("Aceita Ho")
            else:
                myFile.write("Não aceita Ho")

            myFile.close()

            message = "Arquivo: " + path.join(self.__output_folder, self.__file_name + "_PERMUTACOES.TXT") + " criado com sucesso"
        except:
            raise Exception("Could not open the file")
            return False
        finally: 
            print(message)

        
            

    def permutate(self, lines):
        a = [0, 0, 0, 0, 0, 0]
        j = 1
        for i in range(0, len(lines)):
            if(j == 3):
                if(lines[i - 2] < lines[i-1] and lines[i - 1]<lines[i]):
                    a[0] = a[0] + 1
                
                if(lines[i - 2] < lines[i] and lines[i] < lines[i - 1]):
                    a[1] = a[1] + 1
                
                if(lines[i - 1] < lines[i - 2] and lines[i - 2] < lines[i]):
                    a[2] = a[2] + 1
                
                if(lines[i - 1] < lines[i] and lines[i] < lines[i-2]):
                    a[3] = a[3] + 1
                
                if(lines[i] < lines[i - 2] and lines[i - 2] < lines[i - 1]):
                    a[4] = a[4] + 1
                
                if(lines[i] < lines[i-1] and lines[i-1] < lines[i-2]):
                    a[5] = a[5] + 1

                j = 1
            else:
                j = j + 1

        return a
            

    def readFileAsArray(self):
        lines = False
        try:
            myFile = open(self.__file_name + ".TXT", "r")
            lines = myFile.readlines()
            myFile.close()
        except:
            raise Exception("Could not open the file")
        finally:          
            return lines


