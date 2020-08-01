# -*- coding: utf-8 -*-
import math  
from collections import Counter

class Corrida:
   
    def __init__(self, sequencia):
        self.__sequencia = sequencia
         
    def corridaAscendente(self, sequencia):
        __asc = []
        __freqAsc = []
        __i = 0
        __count = 1
        __asc.append(sequencia[0])
        while __i < len(sequencia):
            if((__i+1) >= len(sequencia)):
                __freqAsc.append(__count)
                break
            if sequencia[__i+1] < sequencia[__i]:
                __freqAsc.append(__count)
                __count = 1
                __i+=2
                if(__i >= len(sequencia)):
                    break
                else:
                    __asc.append(sequencia[__i])
            else:
                __count+=1
                __i+=1
                if(__i >= len(sequencia)):
                    break
                else:
                    __asc.append(sequencia[__i])
        
        return __freqAsc
    
    def corridaDescendente(self, sequencia):
        __desc = []
        __freqDesc = []
        __i = 0
        __count = 1
        __desc.append(sequencia[0])
        while __i < len(sequencia):
            if((__i+1) >= len(sequencia)):
                __freqDesc.append(__count)
                break
            if sequencia[__i+1] > sequencia[__i]:
                __freqDesc.append(__count)
                __count = 1
                __i+=2
                if(__i >= len(sequencia)):
                    break
                else:
                    __desc.append(sequencia[__i])
            else:
                __count+=1
                __i+=1
                if(__i >= len(sequencia)):
                    break
                else:
                    __desc.append(sequencia[__i])
                
        return __freqDesc

    def calculaProbabilidadesCorridas(self):     
        asc = self.corridaAscendente(self.__sequencia)
        frequenciaAsc = Counter(asc)
        i = 0
        sumAsc = 0
        sumP = 0
        sumF = 0
        pAsc = []
        gAsc = []
        fxAsc = []
        fAsc = []
        difAsc = []
        while i <= len(frequenciaAsc): 
            sumAsc += frequenciaAsc[i]
            fxAsc.append(frequenciaAsc[i] / math.factorial(frequenciaAsc[i] + 1))
            sumF += fxAsc[i]
            fAsc.append(sumF)
            i += 1

        i = 0
        while i <= len(frequenciaAsc):
            pAsc.append(frequenciaAsc[i]/sumAsc)
            sumP += pAsc[i]
            gAsc.append(sumP)
            difAsc.append(abs(fAsc[i]-gAsc[i]))
            i += 1

        k_asc_calc = max(difAsc)
        k_asc_5 = (1.36/math.sqrt(sumAsc))

        if k_asc_calc < k_asc_5:
            print("Aceita h0 em ascendente", k_asc_calc, " < ", k_asc_5)
        else:
            print("Rejeita h0 em ascendente", k_asc_calc, " > ", k_asc_5)

        desc = self.corridaDescendente(self.__sequencia)
        frequenciaDesc = Counter(desc)
        i = 0
        sumDesc = 0
        sumP = 0
        sumF = 0
        pDesc = []
        gDesc = []
        fxDesc = []
        fDesc = []
        difDesc = []
        while i <= len(frequenciaDesc): 
            sumDesc += frequenciaDesc[i]
            fxDesc.append(frequenciaDesc[i] / math.factorial(frequenciaDesc[i] + 1))
            sumF += fxDesc[i]
            fDesc.append(sumF)
            i += 1

        i = 0
        while i <= len(frequenciaDesc):
            pDesc.append(frequenciaDesc[i]/sumDesc)
            sumP += pDesc[i]
            gDesc.append(sumP)
            difDesc.append(abs(fDesc[i]-gDesc[i]))
            i += 1

        k_desc_calc = max(difDesc)
        k_desc_5 = (1.36/math.sqrt(sumDesc))
        
        if k_desc_calc < k_desc_5:
            print("Aceita h0 em descendente", k_desc_calc, " < ", k_desc_5)
        else:
            print("Rejeita h0 em descendente", k_desc_calc, " > ", k_desc_5)
