# SSO UI Password Renew Notice

Send periodic notifications regarding the expiration date of your Indonesian university account password to your telegram account.


### Run sso-login script locally

Memasang semua dependensi yang diperlukan untuk menjalankan script
```
pip install -r requirements.txt
```

Menjalankan script sso-login
```
python sso-login.py
```


## Built With

* [Python](https://www.python.org/) - Python programming language
* [Pip](https://pip.pypa.io/en/stable/) - Python dependencies manager
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium
* [Django Environ](https://github.com/joke2k/django-environ) - Read secrets and env
* [setup-chromedriver](https://github.com/nanasess/setup-chromedriver) - Github action to setup chrome driver
* [telegram-action](https://github.com/appleboy/telegram-action) - Github action to send telegram message


## Authors

* **Arga Ghulam Ahmad** - *Initial work* - [@argaghulamahmad/sso-ui-renew-notice](https://github.com/argaghulamahmad/sso-ui-renew-notice)