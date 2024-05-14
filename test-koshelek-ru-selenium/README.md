# Тестирование формы регистрации
Стенд: https://koshelek.ru 

- [Запуск тестов Vagrant](#vagrant)
- [Запуск тестов pytest](#pytest)
- [Запуск тестов docker](#docker)

<h3 id="vagrant">Запуск тестов Vagrant</h3>

#### Описание проекта
Данный проект реализована установка сервера с использованием Vagrant, настройка сервера с использованием
Ansible, установкой Allure-server.  
Используемые инструменты:
- VirtualBox Версия 6.1.48 
- Vagrant 2.2.19: vm_box - ubuntu/jammy64
- Ansible core 2.14.10
- Allure-server - dockerhub [kochetkovma/allure-server](https://hub.docker.com/r/kochetkovma/allure-server)

Запуск проекта:
```bash
 ./setup.sh
 ```
Скрипт _setup.sh_ - создает синхронизированный каталог _src_ в корне проекта и запускает _Vagrantfile_. В свою очередь _Vagrantfile_ устанавливает _box ubuntu/jammy64_ и запускает ansible playbook, затем скрипт _allure-report.sh_.
### VAGRANT
#### Пример использования Vagrant
```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

NETWORK_BRIDGE = "enp4s0"
CPUS = 2
MEMORY = 4096
SYNCED_FOLDER = "src/"

$script = <<-SCRIPT
echo "
    ===== setting server ====="
SCRIPT

Vagrant.configure("2") do |config|

    config.vm.box_check_update=false
    config.vm.box = "ubuntu/jammy64"

    config.vm.define "qa" do |qa|
        qa.vm.network "private_network", ip: "192.168.1.100"
        qa.vm.network "public_network", ip: "172.10.10.100", bridge: NETWORK_BRIDGE
        qa.vm.hostname = "qa-test-docker"
        qa.vm.synced_folder SYNCED_FOLDER, "/home/vagrant/src/"
        qa.vm.provider "virtualbox" do |vb|
            vb.gui = false
            vb.memory = MEMORY
            vb.cpus = CPUS
            vb.check_guest_additions = false
            vb.name = "qa-test-docker"
        end
    end

    config.vm.provision "shell", inline: $script
    config.vm.provision "ansible" do |ansible|
    ansible.playbook = "play.yml"
    config.vm.provision "shell", path: "./allure-server/allure-report.sh"
    end

end
```
### ANSIBLE
Роль _ansible_ находится в директории _ansible-role_.  
#### Пример использования Ansible
```ansible
---
# tasks file for qa-test

 - name: Install required system packages
   ansible.builtin.include_tasks: tasks/packages.yml

 - name: Install Docker | docker-compose
   ansible.builtin.include_tasks: tasks/docker.yml

 - name: Clone Github repo
   ansible.builtin.include_tasks: tasks/git.yml

 - name: Running qa-tests | installation allure-server in docker
   ansible.builtin.include_tasks: tasks/run_test.yml
```

### Отчет Allure-server
Запускается скрипт _allure-report.sh_ в котором создается архив zip из результатов allure, затем создается отчет.

#### Пример использования скрипта allure-report.sh
```bash
#!/bin/bash
set -e

echo "
    ==== generate allure report ===="

cd /home/vagrant/src/docker-results

FILE_NAME_ZIP=alluer-report.zip
IP_ADRESS=192.168.1.100
DATA=$(date '+%Y-%m-%d-%H:%M:%S')

zip -5 $FILE_NAME_ZIP * 2>&1

mv $FILE_NAME_ZIP /home/vagrant/src 2>&1

cd /home/vagrant/src 2>&1

RESULT=$(curl -X 'POST' \
          'http://'$IP_ADRESS':8080/api/result' \
          -H 'accept: */*' \
          -H 'Content-Type: multipart/form-data' \
          -F 'allureResults=@'$FILE_NAME_ZIP';type=application/zip' | \
          python3 -c "import sys, json; print(json.load(sys.stdin)['uuid'])")



curl -X 'POST' \
  'http://'$IP_ADRESS':8080/api/report' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "reportSpec": {
    "path": [
      "master",
      "'$DATA'"
    ],
    "executorInfo": {
      "name": "string",
      "type": "string",
      "url": "string",
      "buildOrder": 0,
      "buildName": "#'$DATA'",
      "buildUrl": "string",
      "reportName": "string",
      "reportUrl": "string"
    }
  },
  "results": [
    "'$RESULT'"
  ],
  "deleteResults": true
}'
```

<h3 id="pytest">Запуск тестов pytest</h3>

Системные требования для проведения тестов:
- Linux Ubuntu 22.04.4 LTS
- Python 3.10
- Браузер __Google Chrome__ Версия 122.0.6261.111 (Официальная сборка), (64 бит)
  
Установка файла __requirements.txt__
```bash
pip3 install -r requirements.txt
```
При запуске тестов указываем маркер __-m pairs__ и директорию __--alluredir=allure-results__ для составления отчетов
```bash
pytest -v -m screenshot --alluredir=allure-results
```
Файл __conftest.py__ фикстура __def get_chrome_options()__ должна иметь следующий вид:

```python
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # options.add_argument("--window-size=1920,1080")
    options.add_argument('--start-maximized')
    return options
```

### markers:
````
space: тесты с пробелами (не будут выбраны при запуске с '-m "not space"')
screenshot: тесты с использованием screenshot (не будут выбраны при запуске с '-m "not screenshot"')
pairs: тест с использованием pairwise (не будут выбраны при запуске с '-m "not pairs"')
checkbox: тесты проверки checkbox пользовательское соглашение (не будут выбраны при запуске с '-m "not checkbox"')
username: тесты проверки всплывающего окна Имя пользователя недействительно (не будут выбраны при запуске с '-m "not username"')
all_tests: запуск всех тестов
````

<h3 id="docker">Запуск тестов docker</h3>

Перед запуском тестов в docker:
- В корне проекта создать директорию __doker-result__,
- Обязательно файл __conftest.py__ фикстура __def get_chrome_options()__ должна иметь следующий вид:  
```python
@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    # options.add_argument('chrome')
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    # options.add_argument('--start-maximized')
    return options
```
Запуск тестов в docker:
````
sudo docker-compose up -d
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
#####
![allure_4](https://github.com/MaximRock/Python/assets/95434302/ad05976a-c231-4738-a1f5-ea7db6e51119)
#####
![allure_1](https://github.com/MaximRock/Python/assets/95434302/05f1074a-449b-4a7d-a33d-7898d930343d)
####
Тест с маркером __screenshot__:
######
![allure_2](https://github.com/MaximRock/Python/assets/95434302/c1fa6e1d-deec-4aec-9307-1ee3b03acb04)
######
Каждый тест снабжен скриншотом во вкладке __Tear down__.
######
Пример отчета:
######
![allure_3](https://github.com/MaximRock/Python/assets/95434302/62f6f1b5-1a3e-46c6-9835-3172bf8aadf3)
