import GeradorCongruencial as gc
import TesteCorrida as tc
import TesteIntervalo as ti
import TesteUniformidade as tu

import math 



def main():
    #Ordem argumentos a, m, c
    gerador1 = gc.GeradorLinear( 2921256 , 2**89 - 1, 0, 500)
    list_gerador = gerador1.rand(1000000, "CRIALEO_Gerador1")
    corrida1 = tc.Corrida(list_gerador)
    corrida1.calculaProbabilidadesCorridas()
    print("Tempo total gerador1: ", gerador1.getTotalTime())


    geradorDEC = gc.GeradorLinear(69069, 2**32-1, 1, 500)
    list_gerador = geradorDEC.rand(1000000, "CRIALEO_GeradorDEC")
    corrida2 = tc.Corrida(list_gerador)
    corrida2.calculaProbabilidadesCorridas()
    print("Tempo total geradorDEC: ", geradorDEC.getTotalTime())

    geradorSAS = gc.GeradorLinear(397204094, 2**31-1, 0, 500)
    list_gerador = geradorSAS.rand(1000000, "CRIALEO_GeradorSAS")
    corrida3 = tc.Corrida(list_gerador)
    corrida3.calculaProbabilidadesCorridas()
    print("Tempo total geradorSAS: ", geradorSAS.getTotalTime())
    
    digito = 1
    ti.TesteIntervalo("CRIALEO_Gerador1.TXT", digito)
    ti.TesteIntervalo("CRIALEO_GeradorDEC.TXT", digito)
    ti.TesteIntervalo("CRIALEO_GeradorSAS.TXT", digito)

    tu.TesteUniformidade("CRIALEO_Gerador1.TXT", 10, False)
    tu.TesteUniformidade("CRIALEO_GeradorDEC.TXT", 10, False)
    tu.TesteUniformidade("CRIALEO_GeradorSAS.TXT", 10, False)


   
  
if __name__ == "__main__":
    main()
