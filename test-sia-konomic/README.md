## Тестирование формы регистрации
https://exchange.konomik.com/authorization/signup

###Установка Selenium 
```
pip install webdriver-manager
```
###Установка файла requiremets.txt
````
pip install -r requirements
````
###Запуск тестов
````
pytest -s -v tests/test_page.py::TestPage::<test>
````