from bs4 import BeautifulSoup
import requests

def parse():
    text = str()
    url = 'https://omsk.rabota.ru/?query=python&sort=relevance' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    #print(page.status_code) # Выводим на экран статус-код запроса на адрес(200 - успешный)
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    mydivs = soup.find_all("header", {"vacancy-preview-card__header"}) #ищем необходимый блок с информацией
    for data in mydivs:
        text = data.text.strip()
        text = text.replace("\n", " ") #заменить разрывы строк на пробелы
        text = text.replace("\r", " ") #заменить возврат каретки на пробелы
        text = text.replace("                ", " ") #заменить возврат каретки на пробелы
        text = text.replace("    ", "\n") #заменить возврат каретки на пробелы
        print(text) #вывести полученную информацию на терминал

if __name__ == '__main__':
    parse()