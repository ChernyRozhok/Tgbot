import time, hashlib, requests

from config import PID, KEY

query = 'pid=' + PID + '&method=getRandItem&uts=' + str(int(time.time()))  # формируем строку параметров
signature = hashlib.md5((query + KEY).encode())  # получаем цифровую подпись
url = 'http://anecdotica.ru/api?' + query + '&hash=' + signature.hexdigest()


def return_joke():
    response = requests.get(url)
    response_dict = eval(response.text)
    print(response_dict)
    joke = response_dict['item']['text']
    return joke
