from src.AnaliseDados.analisador import Analisador
from src.LeituraDeArquivos.Leitor import Leitor
import os

class Menu:
    def __init__(self, analisador: Analisador):
        self.analisador = analisador
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
                            self.selecionarAnalise(linhas)
            except:
                print("Erro ao executar opção.")
        pass

    def selecionarAnalise(self, linhas):
        op = int(input('Qual análise deseja visualizar?\n1- Contagem de acessos por IP.\n2- Principais agentes de usuário\n3- Páginas mais acessadas\n'))
        dados = None
        match op:
            case 1:
                dados = self.analisador.pegarNumeroAcessosPorIp(linhas)
                pass
            case 2:
                dados = self.analisador.pegarAgentesDeUsuarioOrdenados(linhas)
                pass
            case 3:
                dados = [item for item in self.analisador.pegarPaginasMaisAcessadas(linhas) if not bool(item['arquivoestatico'])]
                pass
        print(dados)