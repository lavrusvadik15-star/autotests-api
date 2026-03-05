import time


#Возвращает кол-во секунд с 1970 года
def get_random_email() -> str :
    return f"test.{time.time()}@example.com"
#print(time.time())
