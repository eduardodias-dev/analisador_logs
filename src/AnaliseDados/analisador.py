import re
from src.AnaliseDados.models.LogApache import LogApache
from src.AnaliseDados.models.LogApache import LogApacheMapper
class Analisador:
    def __init__(self):
        pass

    #Mapeia as linhas a partir de uma lista
    def mapearLinhas(self, linhas: list):
        listaLogs = []
        mapper = LogApacheMapper()
        listaLogs = [mapper.converterAPartirDaLinha(linha) for linha in linhas]
        return listaLogs
    
    #contar o número de acessos por IP
    def pegarNumeroAcessosPorIp(self, linhas: list):
        if len(linhas) > 0: 
            listaIps = (str(linha).split('- -')[0].strip() for linha in linhas) 
            ipsUnicos = {}
            for ip in listaIps:
                if ipsUnicos.get(ip, None) == None:
                    ipsUnicos[ip] = 1
                else:
                    ipsUnicos[ip] += 1

            return ipsUnicos
        else:
            print("Arquivo não contém linhas.")
            return None

    
    #identificar os principais agentes de usuário
    def pegarAgentesDeUsuarioOrdenados(self, linhas):
        try:
            listaLogs = self.mapearLinhas(linhas)

            dicionario = {}

            for log in listaLogs:
                if dicionario.get(log.userAgent, None) == None:
                    dicionario[log.userAgent] = 1
                else:
                    dicionario[log.userAgent] += 1

            listaOrdenada = [{'nome': userAgent[0], 'numAcessos':userAgent[1]} for userAgent in dicionario.items()]
            listaOrdenada.sort(key= lambda x : x['numAcessos'], reverse=True)
            
            return listaOrdenada
        except Exception as e:
            print('Erro inesperado ao ordenar agentes de Usuário. {}'.format(e))

    #Pegar as páginas mais acessadas
    def pegarPaginasMaisAcessadas(self, linhas):
        try:
            listaLogs = self.mapearLinhas(linhas)
            dicionario = {}

            for log in listaLogs:
                #print('rota {}'.format(log['rota']))

                if dicionario.get(log.pagina, None) == None:
                    dicionario[log.pagina] = 1
                else:
                    dicionario[log.pagina] += 1

            listaOrdenada = [{'pagina': pagina[0], 'numAcessos':pagina[1], 'arquivoestatico': self.verificarSeArquivoEstatico(pagina[0])} for pagina in dicionario.items()]
            listaOrdenada.sort(key= lambda x : x['numAcessos'], reverse=True)
            
            return listaOrdenada
            
        except Exception as e:
            print('Erro inesperado ao pegar as páginas mais acessadas. {}'.format(e))
        pass

    def verificarSeArquivoEstatico(self, rota):
        re.sub(r'\?.*', '', rota)
        padrao = r'\.\w+'

        return True if re.search(padrao, rota) else False
