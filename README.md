# website_tululu_libarary
## Онлайн библиотека книг с сайта [tululu.org](https://tululu.org/) жанра ["научная фантастика"](https://tululu.org/l55/)
Проект позволяет публиковать заранее подготовленные с помощью [парсера](https://github.com/kostyamorales/tululu_library) книги в виде онлайн библиотеки.

![Alt text](screenshot/site.png?raw=true "Optional Title")


Посмотреть пример работы можно в [GitHub Pages](https://kostyamorales.github.io/website_tululu_library/pages/index1.html).

## Подготовка к работе
Для начала определитесь с книгами, которые хотите видеть в вашей библиотеке и скачайте их используя парсер [tululu_library](https://github.com/kostyamorales/tululu_library).
При скачивании в качестве опционального аргумента `dest_folder` укажите корневой каталог данной программы. Пример:
```
python main.py --start_page 1 --end_page 5 --dest_folder /home/morales/PycharmProjects/website_tululu_library
```  

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
## Запуск программы
Запустите программу командой:
```
python render_website.py
```
После этого переходите по [ссылке](http://127.0.0.1:5500/) и пользуйтесь вашей библиотекой.

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org.](https://dvmn.org/)
