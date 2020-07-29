import GeradorCongruencial as gc


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
  
if __name__ == "__main__":
    main()
