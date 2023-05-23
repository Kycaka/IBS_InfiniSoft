# Техническое задание для вакансии "QA Python инженер" в IBS InfiniSoft

## Test_Task

Необходимо на Python + PyTest написать тесты, где реализовать следующие пункты:
1) Написать позитивные и негативные API тесты, которые представлены на главной странице как образец
2) Написать WEB тесты с главной страницы + добавить проверку, что при нажатии на кнопку отправки образца запроса, получаемый результат (тело ответа и статус код) такой же как и через API запрос
3) Все тесты параметризировать и добавить фикстуры
4) Добавить возможность масштабировать проект (К примеру: если в WEB - добавится новая страница, а в API добавится новая версия API. То в таком случае добавляется новый класс и не нарушается текущая реализация)
