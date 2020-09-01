Requests for Bank Products
==============

###Содержание:

####[Старт проекта](#start)
####[Установка и запуск веб-приложения](#webbapp) 
####[Запуск бота в телеграмм @requests_for_bank_products_bot](#bot) 
####[Разворачивание удаленной базы MongoDB с помощью Atlas](#db) 



##<a name="start">Старт проекта</a> 

####Склонируйте репозиторий в папку с Вашими проектами с помощью консольной команды:

```
$ git clone https://github.com/xkxixnxgx/requests_for_bank_products.git
```

##<a name="webbapp">Установка и запуск веб-приложения</a> 

####Перейдите в каталог webbapp_for_operator. Установите виртуальное окружение в каталоге проекта и активируйте его:

```
$ puthon -m venv env
$ source env/bin/activate
```

####Установите необходимые зависимости:

```
$ pip install -r requirements.txt
```

####Запустите сервер с помощью скрипта:

```
$ ./web_run.sh
```

####В строке браузера введите адрес:

http://127.0.0.1:5000/user/requests


##<a name="bot">Запуск бота в телеграмм @requests_for_bank_products_bot</a>

##<a name="db">Разворачивание удаленной базы MongoDB с помощью Atlas</a>