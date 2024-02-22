class Leitor:
    def __init__(self, encoding = 'utf-8'):
        self.encoding = encoding
        pass

    def lerLinhasArquivo(self, caminho) -> list:
        try:
            linhas = []
            with open(caminho, 'r', encoding=self.encoding) as arquivo:
                linhas = arquivo.readlines()

            return linhas
        
        except FileNotFoundError as e:
            print('Arquivo não encontrado {}'.format(e.strerror))
        except Exception as e:
            print('Erro inesperado ao abrir o arquivo: {}'.format(e))
        pass
    
    def lerArquivoComoTexto(self, caminho) -> str:
        try:
            conteudo = ''
            with open(caminho, 'r', encoding=self.encoding) as arquivo:
                conteudo = arquivo.read()

            return conteudo
        
        except FileNotFoundError as e:
            print('Arquivo não encontrado {}'.format(e.strerror))
        except Exception as e:
            print('Erro inesperado ao abrir o arquivo: {}'.format(e))
        pass
