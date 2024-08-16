'''
📖 Docker - це інструмент, який допомагає розробникам створювати, відправляти та запускати свої програми у специфічному середовищі, яке називається контейнером.

Контейнери (containers) – це засоби інкапсуляції застосунку разом з його залежностями.


https://hub.docker.com/

docker run
docker build
docker push 

docker version

docker pull _ завантажити образ docker
docker run _ запустити образ docker як контейнер
docdocker build _ створити образ docker
docker ps _ вивести список контенерів
docker exec _ виконання команди в контейнері
docker cp _ копіювання файлів контейнер-хост
docker images _ перегляд доступних образів


Команда docker exec дозволяє виконувати команди в запущеному контейнері. 

Щоб увійти в контейнер та отримати оболонку shell, ви можете використовувати наступну команду:
docker exec -it [CONTAINER_ID_OR_NAME] /bin/sh

Щоб копіювати файли з контейнера на вашу локальну машину, ви можете використовувати команду docker cp:
docker cp [CONTAINER_ID_OR_NAME]:/path/in/container /local/path



'''

'''

Команда docker pull завантажує вказаний образ із реєстру Docker на локальний комп'ютер:
docker pull image:tag

docker pull image:tag

'''

'''

Наприклад, щоб завантажити образ MySQL, потрібно виконати наступну команду.


'''

'''
1. завантаженнЯ образу
docker pull image:tag (Наприклад, щоб завантажити образ MySQL, потрібно виконати наступну команду.)

2. Після завантаження образу (командою pull) необхідно виконати його запуск командою docker run
docker run [options] image:tag [command, args]




'''
