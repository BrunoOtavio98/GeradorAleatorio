import GeradorCongruencial as gc
import TesteIntervalo as ti
import TesteUniformidade as tu
from TestePermutacoes import TestePermutacoes


digito = 1
ti.TesteIntervalo("CRIALEO_Gerador1.TXT", digito)
ti.TesteIntervalo("CRIALEO_GeradorDEC.TXT", digito)
ti.TesteIntervalo("CRIALEO_GeradorSAS.TXT", digito)

tu.TesteUniformidade("CRIALEO_Gerador1.TXT", 10, False)
tu.TesteUniformidade("CRIALEO_GeradorDEC.TXT", 10, False)
tu.TesteUniformidade("CRIALEO_GeradorSAS.TXT", 10, False)


tp = TestePermutacoes()
tp.setFileName("CRIALEO_Gerador1")
tp.test()
tp.setFileName("CRIALEO_GeradorDEC")
tp.test()
tp.setFileName("CRIALEO_GeradorSAS")
tp.test()