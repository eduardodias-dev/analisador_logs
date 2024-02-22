class Analisador:
    def __init__(self):
        pass

    #contar o número de acessos por IP
    def contarNumeroAcessosPorIp(self, linhas: list):
        if len(linhas) > 0: 
            listaIps = (str(linha).split('- -')[0].strip() for linha in linhas) 
            ipsUnicos = {}
            for ip in listaIps:
                if ipsUnicos.get(ip, None) == None:
                    ipsUnicos[ip] = 1
                else:
                    ipsUnicos[ip] += 1

            print(ipsUnicos)
        else:
            print("Arquivo não contém linhas.")