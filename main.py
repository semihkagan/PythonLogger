from faker import Faker
from colorama import Fore, Back, Style, init
from logger import Logger

init(autoreset=True)
logger = Logger(True,"logs/log.log","logs")

if __name__ == "__main__":
    logger.log("Normal Bir Cikti.")
    logger.info("Bilgi Iceren Bir Cikti.")
    logger.warn("Uyari Iceren Bir Cikti!")
    logger.err("Hata Iceren Bir Cikti!!!")

