import requests
import sys
import random


def make_and_randomize_http_request(spisok):      # Сделать рандомный http запрос
    try:
        random_index=random.randint(0,len(spisok)-1)
        url=f'https://httpstat.us/{spisok[random_index]}'
        response = requests.get(url, timeout=5)
        
        if spisok[random_index]<400:
            log_message=(f"\nУспешный запрос (код {response.status_code}):\n"
                         f"URL: {url}\n"
                         f"Тело ответа: {response.text}")
            print(log_message)

        else:
            raise Exception(f"Ошибка! Код: {response.status_code}, Ответ: {response.text}")
    
    except requests.exceptions.RequestException as e:
        print(f"\nОшибка соединения: {str(e)}", file=sys.stderr)
    
    except Exception as e:
        print(f"\n{str(e)}", file=sys.stderr)


spisok_status_code_100 = [100,101,102,103]
spisok_status_code_200 = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
spisok_status_code_300 = [300, 301, 302, 303, 304, 305, 307, 308]
spisok_status_code_400 = [400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 428, 429, 431, 440, 444, 449, 450, 451, 460, 463, 494, 495, 496, 497, 498, 499]
spisok_status_code_500 = [500, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 520, 521, 522, 523, 524, 525, 526, 527, 530, 561]

all_status_lists = [              # Собираем все списки в один для более удобного использования в цикле
    spisok_status_code_100,
    spisok_status_code_200,
    spisok_status_code_300,
    spisok_status_code_400,
    spisok_status_code_500
]

for i in range(0,5):  # Вызываем цикл, для того чтобы выбрать списки со статус кодами от 100 до 500 
    make_and_randomize_http_request(all_status_lists[i])

