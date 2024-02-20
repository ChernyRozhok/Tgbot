import time, hashlib, requests


PID = 'u02a9862w7248nh6qvzv'              # имя профиля
KEY = '3ec23971b645b541d50c1fb0a683e1f384bfeaca319ceec0fc91cdb26ff53654'  # секретный ключ

query = 'pid=' + PID + '&method=getRandItem&uts=' + str(int(time.time()))  # формируем строку параметров
signature = hashlib.md5((query + KEY).encode())  # получаем цифровую подпись
url = 'http://anecdotica.ru/api?' + query + '&hash=' + signature.hexdigest()


def return_joke():
    response = requests.get(url)
    response_dict = eval(response.text)
    print(response_dict)
    joke = response_dict['item']['text']
    return joke
