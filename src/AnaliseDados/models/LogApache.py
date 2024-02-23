import re
class LogApache:
    def __init__(self, ip='', data='', rota='', metodo='', protocolo='', size='', userAgent='', statusCode=''):
        self.ip = ip
        self.data = data
        self.rota = rota
        self.metodo = metodo
        self.protocolo = protocolo
        self.size = size
        self.userAgent = userAgent
        self.statusCode = statusCode

class LogApacheMapper:
    def converterAPartirDaLinha(self, linha:str):
        logApache = LogApache()

        stringsNaLinha = self.__extrairStrings(linha, '\"', '\"')
        data = self.__extrairStrings(linha, '[', ']')
        numeros = self.__extrairComRegex(linha, r'\s\d+')

        logApache.statusCode = int(numeros[0])
        logApache.ip = linha.split('- -')[0].strip()
        logApache.data = data[0]
        logApache.rota = str(stringsNaLinha[0]).split(' ')[1]
        logApache.metodo = str(stringsNaLinha[0]).split(' ')[0]
        logApache.protocolo = str(stringsNaLinha[0]).split(' ')[2]
        logApache.userAgent = stringsNaLinha[-1]
        
        return logApache

    def __extrairStrings(self, texto, delimitador_aberto, delimitador_fechado):
        regex = re.compile(rf'{re.escape(delimitador_aberto)}(.*?)'
                            rf'{re.escape(delimitador_fechado)}')
        
        resultados = re.findall(regex, texto)
        return resultados

    def __extrairComRegex(self, texto, expressao):
        regex = re.compile(expressao)

        resultados = re.findall(regex, texto)
        return resultados