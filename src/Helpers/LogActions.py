import logging
import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

filePath = "logs/log_app.log"
logging.basicConfig(filename=filePath, encoding='utf-8', level = logging.DEBUG, format="%(asctime)s: %(levelname)s %(message)s")

def adicionarAoLog(nomeFuncao):
    def adicionarAoLogReal(funcao):
        def wrapper(*args, **kwargs):
            logging.info("Chamando a função {}.".format(nomeFuncao))
            return funcao(*args, **kwargs)
        return wrapper
    return adicionarAoLogReal
