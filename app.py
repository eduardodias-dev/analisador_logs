from src.UI.menu import Menu
from src.AnaliseDados.analisador import Analisador
from src.LeituraDeArquivos.Leitor import Leitor

import json

# menu = Menu()

# menu.executar()
leitor = Leitor()
analisador = Analisador()

linhas = leitor.lerLinhasArquivo('data/teste.log')
#analisador.contarNumeroAcessosPorIp(linhas)
analisador.mapearLinhas(linhas)
