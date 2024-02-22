from src.LeituraDeArquivos.Leitor import Leitor
import os

class Menu:
    def __init__(self):
        pass

    def executar(self):
        op = 0
        while op != 2:
            try:
                op = int(input('''Digite a opção desejada:\n1-Analisar logs\n2-Sair\n'''))
                os.system('cls')
                match op:
                    case 1:
                        caminhoArquivo = input('Digite o caminho do arquivo:\n')
                        if len(caminhoArquivo) <= 0 or caminhoArquivo == None:
                            print('Caminho inválido.')
                            continue
                        else:
                            leitor = Leitor()
                            linhas = leitor.lerLinhasArquivo(caminhoArquivo)

                            for ind in range(10):
                                print(linhas[ind])
            except:
                print("Erro ao executar opção.")
        pass