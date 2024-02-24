import json
from src.AnaliseDados.models.LogApache import LogApache
from src.AnaliseDados.models.LogApache import LogApacheMapper
class Analisador:
    def __init__(self):
        pass

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

    def mapearLinhas(self, linhas: list):
        listaLogs = []
        mapper = LogApacheMapper()
        
        #listaLogs = [mapper.converterAPartirDaLinha(linha).__dict__ for item, linha in enumerate(linhas) if item < 6]
        listaLogs = [mapper.converterAPartirDaLinha(linha) for linha in linhas]
        return listaLogs
    
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