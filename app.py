import json
from src.UI.menu import Menu
from src.AnaliseDados.analisador import Analisador
from src.LeituraDeArquivos.Leitor import Leitor

menu = Menu(Analisador())
menu.executar()
# leitor = Leitor()
# analisador = Analisador()

# linhas = leitor.lerLinhasArquivo('data/teste.log')

# paginas = analisador.pegarPaginasMaisAcessadas(linhas)

# print(json.dumps(paginas, indent=2))