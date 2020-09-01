Requests for Bank Products
==============

###Содержание:

####[Старт проекта](#start)
####[Установка и запуск веб-приложения](#webbapp) 
####[Запуск телеграмм бота @requests_for_bank_products_bot](#bot) 
####[Разворачивание удаленной базы MongoDB с помощью Atlas](#db) 



##<a name="start">Старт проекта</a> 

####Склонируйте репозиторий в папку с Вашими проектами с помощью консольной команды:

```
$ git clone https://github.com/xkxixnxgx/requests_for_bank_products.git
```

##<a name="webbapp">Установка и запуск веб-приложения</a> 

####Перейдите в каталог /webbapp_for_operator. Установите виртуальное окружение в каталоге проекта и активируйте его:

```
$ puthon -m venv env_webapp
$ source env_webapp/bin/activate
```

####Установите необходимые зависимости:

```
$ pip install -r requirements.txt
```

####Создайте в каталоге /webbapp_for_operator файл settings.py с настройками. Подставьте свои ключи шифрования и ключ доступа к удаленной базе данных. Либо воспользуйтесь теми, что в примере ниже:

```
# keys for encrypt
pubkey_pem = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6BPiu\n+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qedInq\nmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaEFfnP\nRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGwHxJA\nZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5wWvf\nyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQAB\n-----END RSA PUBLIC KEY-----\n'
privkey_pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqQIBAAKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6\nBPiu+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qe\ndInqmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaE\nFfnPRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGw\nHxJAZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5\nwWvfyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQABAoIBAQCBwdSVyFWSYQy7\nx9z5ENF24veh2x+VFKJyWRRtls4NHIYpDz53wLsmcaqlMZvfrdWE0FqARz9EIjwW\ns2HefW8otjEiQTiTJ38g8yOAbcqbUT8M+AHvWda30i0T0dq5hDq36axqTV9Fa3M7\n7TobGb28gw9vC2oUE5FSVOwwb1DX6/42nIor1SewSTiglE3smeTsDjUL16I+fTDo\n+ksKA/QUpwFXSy+GQAfa55ME/YaQpvYcbi8uLAj0kpd1eEib52Jxwgm+DcmV6riN\nGzh4+4LhjNZwzJJ73EHtloPhJvUx+dOpxtNi1/BXOQfZZlDrP2G+hn+BEXmccd4F\noGS43syBAoGJAJIJhh8EFMtek50SdUsmBFXRMWH4f8rQx5XaBr2kc9lAYNg/mIGK\n3BcmcXqolAeepg4Z41/ZYfDQSLR65DUlJJi50lLUb3IhkobTXpIGY9gwbsZy6zuu\nFFOy07isTWs8YJeF43nVRxqs+Zbkbua3wYbVkxRImSXxujtTxpVyDr9WsLECekHV\nSWsCeQDzBldszgmMOkXP92XghWiVBu8Oq3DCPQreb2tfJc/1INdINLO0douvT+2u\nfSJSPlhagT8WNRyvkFhMmNeheHDfn4ifZJuvKMmuhvAH9aWYJ1k/gu+X4VfA4jm7\n/Fcka8m63rU3+f/4h9OHei8bRQv1uGVTfM6nzjECgYh7mRntqDudQAd5GgUxvBRR\nOYMtIu+tjPROzL+Fw+jUx5rviyudABR0d3H12TWoGUr7hkedeNNeyDmwno4EuNH3\nfNYYinlkRCvKdpyExGm+sIcg6GRVF2lWyXRNyW6gwvIRbBzxoWPTnPCFGAMQvBdL\n8fjQYv1TUvpGegoJtAXtRQa4WZt1mnnPAngLm0/tmGGIWvgemJg7AuQdyfj84F9A\nR54PRY8BOlMWR/1AK5QxmD/PnaeiX8OV3fhmSinzK5I1KFWvQtV5lsD9TSc/RZTR\n5sbLGRK5rpe8DpUKnXxH6rFAOw261rBqwuMdk6lgBQaeng4SOFmrmb6ae7YLKLjN\n9uECgYgjBh9fVQwiyy1eeEqqAFFX1IdR2v9QljwtwB4vEISCXB6l2Iz4gBEbZnlK\nSMKof+SqwouIX9BLQxIFNY19t+IeBGPCJUKhgQcZpUNbQq9mY10JMElqtGCpDVju\nL0pR/1oFIe+E/hnei5wRPEMf+tIAfgBv3ayvwS5PgOCh5h1oCNvZt7hBm7bo\n-----END RSA PRIVATE KEY-----\n'


# key of MongoDB in Atlas
CONNECTION_STRING = 'mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority'
```

####Запустите сервер с помощью скрипта:

```
$ ./run_web.sh
```

####В строке браузера введите адрес:

http://127.0.0.1:5000/user/requests


##<a name="bot">Запуск телеграмм бота @requests_for_bank_products_bot</a>

####Создайте в каталоге /botWhileTrue файл settings.py с настройками. Подставьте свои ключи шифрования и ключ доступа к удаленной базе данных. Либо воспользуйтесь теми, что в примере ниже:

```
# keys for encrypt
pubkey_pem = b'-----BEGIN RSA PUBLIC KEY-----\nMIIBCgKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6BPiu\n+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qedInq\nmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaEFfnP\nRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGwHxJA\nZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5wWvf\nyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQAB\n-----END RSA PUBLIC KEY-----\n'
privkey_pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEqQIBAAKCAQEAiqKoZ+O8EUFz7OvjFxQPUt65FogPjzvphp38QUlRXYvboXf6\nBPiu+zqd2if4MVIa9HSnV3dgL/NyeTp7G7Ex/YSscv86KbOVy7DjyR22BH1yh2qe\ndInqmv1EFfbyJDikpuPSec5CSUOQDGwRVF65bYgWgxeGu9zViqr7BF7Z2GTlUvaE\nFfnPRnXcUPaEeOWiz72yMLoiszuE4ov3ReIMobkdDlkWNxBsAqUk//Dr9d52TvGw\nHxJAZ5qPzTZGSd8RlN9ox+yBCSBo0nfADt8EHBf8FBuxqgp+MvKDTrYer1uJIPN5\nwWvfyPdGT0/41jhOTXWYk1e8Dh8p7q5rObQnewIDAQABAoIBAQCBwdSVyFWSYQy7\nx9z5ENF24veh2x+VFKJyWRRtls4NHIYpDz53wLsmcaqlMZvfrdWE0FqARz9EIjwW\ns2HefW8otjEiQTiTJ38g8yOAbcqbUT8M+AHvWda30i0T0dq5hDq36axqTV9Fa3M7\n7TobGb28gw9vC2oUE5FSVOwwb1DX6/42nIor1SewSTiglE3smeTsDjUL16I+fTDo\n+ksKA/QUpwFXSy+GQAfa55ME/YaQpvYcbi8uLAj0kpd1eEib52Jxwgm+DcmV6riN\nGzh4+4LhjNZwzJJ73EHtloPhJvUx+dOpxtNi1/BXOQfZZlDrP2G+hn+BEXmccd4F\noGS43syBAoGJAJIJhh8EFMtek50SdUsmBFXRMWH4f8rQx5XaBr2kc9lAYNg/mIGK\n3BcmcXqolAeepg4Z41/ZYfDQSLR65DUlJJi50lLUb3IhkobTXpIGY9gwbsZy6zuu\nFFOy07isTWs8YJeF43nVRxqs+Zbkbua3wYbVkxRImSXxujtTxpVyDr9WsLECekHV\nSWsCeQDzBldszgmMOkXP92XghWiVBu8Oq3DCPQreb2tfJc/1INdINLO0douvT+2u\nfSJSPlhagT8WNRyvkFhMmNeheHDfn4ifZJuvKMmuhvAH9aWYJ1k/gu+X4VfA4jm7\n/Fcka8m63rU3+f/4h9OHei8bRQv1uGVTfM6nzjECgYh7mRntqDudQAd5GgUxvBRR\nOYMtIu+tjPROzL+Fw+jUx5rviyudABR0d3H12TWoGUr7hkedeNNeyDmwno4EuNH3\nfNYYinlkRCvKdpyExGm+sIcg6GRVF2lWyXRNyW6gwvIRbBzxoWPTnPCFGAMQvBdL\n8fjQYv1TUvpGegoJtAXtRQa4WZt1mnnPAngLm0/tmGGIWvgemJg7AuQdyfj84F9A\nR54PRY8BOlMWR/1AK5QxmD/PnaeiX8OV3fhmSinzK5I1KFWvQtV5lsD9TSc/RZTR\n5sbLGRK5rpe8DpUKnXxH6rFAOw261rBqwuMdk6lgBQaeng4SOFmrmb6ae7YLKLjN\n9uECgYgjBh9fVQwiyy1eeEqqAFFX1IdR2v9QljwtwB4vEISCXB6l2Iz4gBEbZnlK\nSMKof+SqwouIX9BLQxIFNY19t+IeBGPCJUKhgQcZpUNbQq9mY10JMElqtGCpDVju\nL0pR/1oFIe+E/hnei5wRPEMf+tIAfgBv3ayvwS5PgOCh5h1oCNvZt7hBm7bo\n-----END RSA PRIVATE KEY-----\n'


# key of MongoDB in Atlas
CONNECTION_STRING = 'mongodb+srv://user1:mb_test12345@cluster0.tmwn7.mongodb.net/mb_test?retryWrites=true&w=majority'

# Token for telegram_bot
token = '1293518313:AAET6K3HObbgrZT_gt2-EAVxqyqoMr2XfQg'
```


##<a name="db">Разворачивание удаленной базы MongoDB с помощью Atlas</a>

####Перейдите по ссылке ниже и запустите кластер базы данных согласно инструкции:
```
https://www.mongodb.com/try
```

####Используйте выданный вам адресс для доступа к удаленной базе из веб-приложения и телеграмм бота, подставляя его в переменную:
```
CONNECTION_STRING = ''
```
