import GeradorCongruencial as gc


def main():
    a = 16807
    m = 2147483647
    c = 1
    
    teste = gc.GeradorLinear(a, m, c, 500)

    list_teste = teste.rand(1000)
    
    print("Tempo total: ", teste.getTotalTime())

if __name__ == "__main__":
    main()
