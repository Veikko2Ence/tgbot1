import logging

logger = logging.getLogger(__name__) #Тут задается имя логера в зависимости от файла ок да?
logger.setLevel(logging.INFO) #Тут крч инфа о предупреждениях, ошибках 

file_write=logging.FileHandler("logs.log")
file_write.setLevel(logging.INFO)

Format = logging.Formatter("%(levelname)s - %(message)s")
Format.setFormatter(Format)
logger.addHandler(file_write) #Все что получилось - пишется в файл (вроде)
