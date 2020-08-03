import GeradorCongruencial as gc
import TesteCorrida as tc
import TesteIntervalo as ti
import TesteUniformidade as tu
from TestePermutacoes import TestePermutacoes
import math 

def main():
    #Ordem argumentos a, m, c
    geradorNOVO = gc.GeradorLinear( 2921256 , 2**89 - 1, 0, 500)
    list_gerador = geradorNOVO.rand(1000000, "CRIALEO_GeradorNovo")
    print("Tempo total gerador novo: ", geradorNOVO.getTotalTime())

    geradorDEC = gc.GeradorLinear(69069, 2**32-1, 1, 500)
    list_gerador = geradorDEC.rand(1000000, "CRIALEO_GeradorDEC")
    print("Tempo total geradorDEC: ", geradorDEC.getTotalTime())

    geradorSAS = gc.GeradorLinear(397204094, 2**31-1, 0, 500)
    list_gerador = geradorSAS.rand(1000000, "CRIALEO_GeradorSAS")
    print("Tempo total geradorSAS: ", geradorSAS.getTotalTime())
    
    gerador1 = gc.GeradorLinear( 16807 , 2**31 - 1, 0, 500)
    list_gerador = gerador1.rand(1000000, "CRIALEO_Gerador1")
    print("Tempo total gerador 1: ", gerador1.getTotalTime())

    tests = []
    testsFile = []

    testsFile.append("CRIALEO_GeradorNovo")
    testsFile.append("CRIALEO_GeradorDEC")
    testsFile.append("CRIALEO_GeradorSAS")
    testsFile.append("CRIALEO_Gerador1")

    tests.append("Novo")
    tests.append("DEC")
    tests.append("SAS")
    tests.append("1")

    num1 = int(input("Digite o digito para o Teste do Intervalo: "))
    num2 = int(input("Digite o numero de intervalos para o Teste de Uniforminade: "))

    i = 0
    print("")
    for t in tests:
        print("Executandos testes para o gerador " + t)
  
        print("Teste das corridas ") 
        tc.Corrida(testsFile[i])
        print("")

        print("Teste do intervalo ")
        
        ti.TesteIntervalo(testsFile[i] + ".TXT", num1)
        print("")

        print("Teste das permutacoes: ")
        tp = TestePermutacoes()
        tp.setFileName(testsFile[i])
        tp.test()
        print("")

        print("Teste de uniformidade")
        
        tu.TesteUniformidade(testsFile[i] + ".TXT", num2, False)
        print("")
        i = i + 1
    input("Precione qualquer tecla para terminar...")
    



if __name__ == "__main__":
    main()
