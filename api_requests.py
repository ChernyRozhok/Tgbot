import time, hashlib, requests


PID = '438652m7c525bjk8dhma'              # имя профиля
KEY = '834ca84295341d9eba832e861a32e10d046d07741025dbf79e92a0f4aa227492'  # секретный ключ

query = 'pid=' + PID + '&method=getRandItem&uts=' + str(int(time.time()))  # формируем строку параметров
signature = hashlib.md5((query + KEY).encode())  # получаем цифровую подпись
url = 'http://anecdotica.ru/api?' + query + '&hash=' + signature.hexdigest()


def return_joke():
    response = requests.get(url)
    response_dict = eval(response.text)
    joke = response_dict['item']['text']
    return joke