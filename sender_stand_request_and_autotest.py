#Гаранин Александр, 11-я когорта — Финальный проект. Инженер по тестированию плюс
import config             #Импортировать файлы из config в этот
import requests           #Импортировать библиотеку requests в этот файл
import data               #Импортировать файлы из data в этот


# Создание заказа
def create_order(body):
    return requests.post (config.URL_SERVICE + config.CREAT_ORDERS,
                         json=body)


# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{config.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response


# Автотест
def test_order():
    response = create_order(data.order_body)  #отправляем запрос на создание заказа

    track_number = response.json()["track"] #получаем нормер созданного заказа
    print("Заказ создан. Номер трека:", track_number) #выводим создание заказа и его номер

    # Получение данных заказа по треку
    order_response = get_order(track_number) #отправляем GET запрос на на получение информации о заказе

    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"  #Проверка на успешный ответ, если ответ не успешен, выводим код ошибки
    order_data = order_response.json()   #Получаем данные о заказе
    print("Данные заказа:")
    print(order_data)   #выводим данные о заказе