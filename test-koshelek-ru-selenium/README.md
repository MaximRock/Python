# Тестирование формы регистрации
Стенд: https://koshelek.ru 

Браузер __Google Chrome__ Версия 122.0.6261.111 (Официальная сборка), (64 бит)

Установка файла requiremets.txt
````
pip3 install -r requirements.txt
````
## Запуск тестов

### Запуск тестов в pytest
При запуске тестов указываем маркер __-m pairs__ и директорию __--alluredir=allure-results__
для составления отчетов
````
pytest -v -m screenshot --alluredir=allure-results
````
### markers:
````
space: тесты с пробелами (не будут выбраны при запуске с '-m "not space"')
screenshot: тесты с использованием screenshot (не будут выбраны при запуске с '-m "not screenshot"')
pairs: тест с использованием pairwise (не будут выбраны при запуске с '-m "not pairs"')
checkbox: тесты проверки checkbox пользовательское соглашение (не будут выбраны при запуске с '-m "not checkbox"')
all_tests: запуск всех тестов
````
### Запуск тестов в docker
Перед запуском тестов в docker обязательно раскомментировать параметр в файле __conftest.py__ 
````
options.add_argument("--headless")
````
Запуск тестов в docker:
````
sudo docker-compose up
````
В файле __docker-compose.py__ так же можно менять маркеры для запуска различных тестов __-m checkbox__:
````
command: ["pytest", "-v", "-m screenshot", "tests/test_page.py", "--alluredir=allure-results"]
````
## ALLURE отчет
При выполнении тестов создается отчет в __allure__, результат располагается в директории __allure-results__,
при использовании __docker__ результат располагается в директории __docker-results__.
Тесты с маркером __screenshot__ сохраняются в директории __screenshot__.
#####
Пример отчета:
######
![allure_1](https://github.com/MaximRock/Python/assets/95434302/05f1074a-449b-4a7d-a33d-7898d930343d)
#####
Тест с маркером __screenshot__:
######
![allure_2](https://github.com/MaximRock/Python/assets/95434302/c1fa6e1d-deec-4aec-9307-1ee3b03acb04)
######
Каждый тест снабжен скриншотом во вкладке __Tear down__.
######
Пример отчета:
######
![allure_3](https://github.com/MaximRock/Python/assets/95434302/62f6f1b5-1a3e-46c6-9835-3172bf8aadf3)
