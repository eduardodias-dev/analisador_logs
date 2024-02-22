from src.LeituraDeArquivos.Leitor import Leitor
import os

leitor = Leitor('utf-8')

linhas = leitor.lerLinhasArquivo('data/aicbrasill.com.br-ssl_log')

for item in range(3):
    print(linhas[item])