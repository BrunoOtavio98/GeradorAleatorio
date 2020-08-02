import GeradorCongruencial as gc
import TesteCorrida as tc


def main():
    #Ordem argumentos a, m, c
    gerador1 = gc.GeradorLinear(16807, 2**31-1, 0, 500)
    list_gerador = gerador1.rand(1000000, "CRIALEO_Gerador1")
    print("Tempo total gerador1: ", gerador1.getTotalTime())

    geradorDEC = gc.GeradorLinear(69069, 2**32-1, 1, 500)
    list_gerador = geradorDEC.rand(1000000, "CRIALEO_GeradorDEC")
    print("Tempo total geradorDEC: ", geradorDEC.getTotalTime())

    geradorSAS = gc.GeradorLinear(397204094, 2**31-1, 0, 500)
    list_gerador = geradorSAS.rand(1000000, "CRIALEO_GeradorSAS")
    print("Tempo total geradorSAS: ", geradorSAS.getTotalTime())

    tc.Corrida("CRIALEO_Gerador1")
    tc.Corrida("CRIALEO_GeradorDEC")
    tc.Corrida("CRIALEO_GeradorSAS")
  
if __name__ == "__main__":
    main()
