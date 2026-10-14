

from time import sleep

from loguru import logger


logger.add("execution_logs.log", format="{time} - {message}", level="INFO", rotation="1 day")


def primeira_atividade():
    logger.info("Iniciando primeira atividade")
    sleep(1)

def segunda_atividade():
    logger.info("Iniciando segunda atividade")
    sleep(1)

def terceira_atividade():
    logger.info("Iniciando terceira atividade")
    sleep(1)


def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    logger.info("Pipeline finalizado")

if __name__ == "__main__":
    while True:
        pipeline()
        sleep(5)  # Adiciona um intervalo de 5 segundos entre cada execução do pipeline