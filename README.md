Requests for Bank Products
==============

### Описание проекта

#### Данный проект был подготовлен в рамках недельного онлайн хакатона Digital SuperHero Online в составе команды из 4 человек.
+ ##### Чернов Игорь - капитан команды, телеграмм бот, API, шифрование, сборка модулей.
+ ##### Александр Репкин - база данных, модели базы данных, шифрование.
+ ##### Андрей Удалов - аналитика, сбор бизнес требований, подготовка презентаций.
+ ##### Бородич Юрий - веб-приложение оператора банка для обработки заявок, база данных, шифрование.

### Цель проекта

#### В рамках направления "Fintech" мы выбрали тему "Интеграция и API". Перед нами стояла задача разработать систему сбора заявок клиентов банка АкБарс посредством мессенджеров, разработать веб-приложение для обработки заявок оператором банка с возможностью принять заявку либо отклонить.

### Проект состоит из трех модулей

#### 1. Веб-приложение, с которым работает оператор банка и может отсортировать заявки, просмотреть заявку более подробно, принять ее либо отклонить.
#### 2. Телеграмм бот, позволяющий клиенту с телефона оформить заявку на любой продукт банка.
#### 3. Nosql база данных MongoDB в облаке

## Как развернуть проект локально:

#### 1. [Подготовка к старту проекта](#start)
#### 2. [Установка и запуск веб-приложения](#webbapp) 
#### 3. [Запуск телеграмм бота @requests_for_bank_products_bot](#bot) 
#### 4. [Разворачивание удаленной базы MongoDB с помощью Atlas](#db) 


## 1. <a name="start">Подготовка к старту проекта</a> 

#### Склонируйте репозиторий в папку с Вашими проектами с помощью консольной команды:

```
$ git clone https://github.com/xkxixnxgx/requests_for_bank_products.git
```


## 2. <a name="webbapp">Установка и запуск веб-приложения</a> 

#### Приложение работает на python 3.8.

#### Перейдите в каталог `/webbapp_for_operator`. Установите виртуальное окружение в каталоге проекта и активируйте его:

```
$ puthon -m venv env_webapp
$ source env_webapp/bin/activate
```

#### Установите необходимые зависимости:

```
$ pip install -r requirements.txt
```

#### Создайте в каталоге `/webbapp_for_operator` файл `settings.py` с настройками. Подставьте свои ключи шифрования и ключ доступа к удаленной базе данных. Либо воспользуйтесь теми, что в примере ниже:

```
# keys for encrypt
pubkey_pem = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6BPiu\n+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qedInq\nmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaEFfnP\nRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGwHxJA\nZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5wWvf\nyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQAB\n-----END RSA PUBLIC KEY-----\n'
privkey_pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqQIBAAKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6\nBPiu+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qe\ndInqmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaE\nFfnPRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGw\nHxJAZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5\nwWvfyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQABAoIBAQCBwdSVyFWSYQy7\nx9z5ENF24veh2x+VFKJyWRRtls4NHIYpDz53wLsmcaqlMZvfrdWE0FqARz9EIjwW\ns2HefW8otjEiQTiTJ38g8yOAbcqbUT8M+AHvWda30i0T0dq5hDq36axqTV9Fa3M7\n7TobGb28gw9vC2oUE5FSVOwwb1DX6/42nIor1SewSTiglE3smeTsDjUL16I+fTDo\n+ksKA/QUpwFXSy+GQAfa55ME/YaQpvYcbi8uLAj0kpd1eEib52Jxwgm+DcmV6riN\nGzh4+4LhjNZwzJJ73EHtloPhJvUx+dOpxtNi1/BXOQfZZlDrP2G+hn+BEXmccd4F\noGS43syBAoGJAJIJhh8EFMtek50SdUsmBFXRMWH4f8rQx5XaBr2kc9lAYNg/mIGK\n3BcmcXqolAeepg4Z41/ZYfDQSLR65DUlJJi50lLUb3IhkobTXpIGY9gwbsZy6zuu\nFFOy07isTWs8YJeF43nVRxqs+Zbkbua3wYbVkxRImSXxujtTxpVyDr9WsLECekHV\nSWsCeQDzBldszgmMOkXP92XghWiVBu8Oq3DCPQreb2tfJc/1INdINLO0douvT+2u\nfSJSPlhagT8WNRyvkFhMmNeheHDfn4ifZJuvKMmuhvAH9aWYJ1k/gu+X4VfA4jm7\n/Fcka8m63rU3+f/4h9OHei8bRQv1uGVTfM6nzjECgYh7mRntqDudQAd5GgUxvBRR\nOYMtIu+tjPROzL+Fw+jUx5rviyudABR0d3H12TWoGUr7hkedeNNeyDmwno4EuNH3\nfNYYinlkRCvKdpyExGm+sIcg6GRVF2lWyXRNyW6gwvIRbBzxoWPTnPCFGAMQvBdL\n8fjQYv1TUvpGegoJtAXtRQa4WZt1mnnPAngLm0/tmGGIWvgemJg7AuQdyfj84F9A\nR54PRY8BOlMWR/1AK5QxmD/PnaeiX8OV3fhmSinzK5I1KFWvQtV5lsD9TSc/RZTR\n5sbLGRK5rpe8DpUKnXxH6rFAOw261rBqwuMdk6lgBQaeng4SOFmrmb6ae7YLKLjN\n9uECgYgjBh9fVQwiyy1eeEqqAFFX1IdR2v9QljwtwB4vEISCXB6l2Iz4gBEbZnlK\nSMKof+SqwouIX9BLQxIFNY19t+IeBGPCJUKhgQcZpUNbQq9mY10JMElqtGCpDVju\nL0pR/1oFIe+E/hnei5wRPEMf+tIAfgBv3ayvwS5PgOCh5h1oCNvZt7hBm7bo\n-----END RSA PRIVATE KEY-----\n'


# key of MongoDB in Atlas
CONNECTION_STRING = 'mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority'
```

#### Запустите сервер с помощью скрипта:

```
$ ./run_web.sh
```

#### В строке браузера введите адрес:

http://127.0.0.1:5000/requests


## 3. <a name="bot">Запуск телеграмм бота `@requests_for_bank_products_bot`</a>

#### Перейдите в каталог `/botWhileTrue`. Установите виртуальное окружение в каталоге проекта и активируйте его:

```
$ python -m venv env_bot
$ source env_bot/bin/activate
```

#### Установите необходимые зависимости:

```
$ pip install -r requirements_bot.txt
```

#### Создайте в каталоге `/botWhileTrue` файл `settings.py` с настройками. Подставьте свои ключи шифрования и ключ доступа к удаленной базе данных. Либо воспользуйтесь теми, что в примере ниже:

```
# keys for encrypt
pubkey_pem = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6BPiu\n+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qedInq\nmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaEFfnP\nRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGwHxJA\nZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5wWvf\nyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQAB\n-----END RSA PUBLIC KEY-----\n'
privkey_pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqQIBAAKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6\nBPiu+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qe\ndInqmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaE\nFfnPRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGw\nHxJAZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5\nwWvfyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQABAoIBAQCBwdSVyFWSYQy7\nx9z5ENF24veh2x+VFKJyWRRtls4NHIYpDz53wLsmcaqlMZvfrdWE0FqARz9EIjwW\ns2HefW8otjEiQTiTJ38g8yOAbcqbUT8M+AHvWda30i0T0dq5hDq36axqTV9Fa3M7\n7TobGb28gw9vC2oUE5FSVOwwb1DX6/42nIor1SewSTiglE3smeTsDjUL16I+fTDo\n+ksKA/QUpwFXSy+GQAfa55ME/YaQpvYcbi8uLAj0kpd1eEib52Jxwgm+DcmV6riN\nGzh4+4LhjNZwzJJ73EHtloPhJvUx+dOpxtNi1/BXOQfZZlDrP2G+hn+BEXmccd4F\noGS43syBAoGJAJIJhh8EFMtek50SdUsmBFXRMWH4f8rQx5XaBr2kc9lAYNg/mIGK\n3BcmcXqolAeepg4Z41/ZYfDQSLR65DUlJJi50lLUb3IhkobTXpIGY9gwbsZy6zuu\nFFOy07isTWs8YJeF43nVRxqs+Zbkbua3wYbVkxRImSXxujtTxpVyDr9WsLECekHV\nSWsCeQDzBldszgmMOkXP92XghWiVBu8Oq3DCPQreb2tfJc/1INdINLO0douvT+2u\nfSJSPlhagT8WNRyvkFhMmNeheHDfn4ifZJuvKMmuhvAH9aWYJ1k/gu+X4VfA4jm7\n/Fcka8m63rU3+f/4h9OHei8bRQv1uGVTfM6nzjECgYh7mRntqDudQAd5GgUxvBRR\nOYMtIu+tjPROzL+Fw+jUx5rviyudABR0d3H12TWoGUr7hkedeNNeyDmwno4EuNH3\nfNYYinlkRCvKdpyExGm+sIcg6GRVF2lWyXRNyW6gwvIRbBzxoWPTnPCFGAMQvBdL\n8fjQYv1TUvpGegoJtAXtRQa4WZt1mnnPAngLm0/tmGGIWvgemJg7AuQdyfj84F9A\nR54PRY8BOlMWR/1AK5QxmD/PnaeiX8OV3fhmSinzK5I1KFWvQtV5lsD9TSc/RZTR\n5sbLGRK5rpe8DpUKnXxH6rFAOw261rBqwuMdk6lgBQaeng4SOFmrmb6ae7YLKLjN\n9uECgYgjBh9fVQwiyy1eeEqqAFFX1IdR2v9QljwtwB4vEISCXB6l2Iz4gBEbZnlK\nSMKof+SqwouIX9BLQxIFNY19t+IeBGPCJUKhgQcZpUNbQq9mY10JMElqtGCpDVju\nL0pR/1oFIe+E/hnei5wRPEMf+tIAfgBv3ayvwS5PgOCh5h1oCNvZt7hBm7bo\n-----END RSA PRIVATE KEY-----\n'

# key of MongoDB in Atlas
CONNECTION_STRING = 'mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority'

# Token for telegram_bot
token = '1293518313:AAET6K3HObbgrZT_gt2-EAVxqyqoMr2XfQg'
```

## 4. <a name="db">Разворачивание удаленной базы MongoDB с помощью Atlas</a>

#### Перейдите по ссылке ниже и запустите кластер базы данных согласно инструкции:
```
https://www.mongodb.com/try
```

#### Используйте выданный вам адресс для доступа к удаленной базе из веб-приложения и телеграмм бота, подставляя его в переменную:
```
CONNECTION_STRING = ''
```

#### Также вы можете воспользоваться уже развернутым кластером, указанным по умолчанию в пунктах 2 и 3 данного руководства:

```
CONNECTION_STRING = 'mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority'
```