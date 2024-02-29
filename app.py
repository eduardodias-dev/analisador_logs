import json
from src.UI.menu import Menu
from src.AnaliseDados.analisador import Analisador
from src.LeituraDeArquivos.Leitor import Leitor

if __name__ == '__main__':
    menu = Menu(Analisador())
    menu.executar()