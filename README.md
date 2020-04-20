# SSO UI Password Renew Notice

![SSO UI Renew Notice](https://github.com/argaghulamahmad/sso-ui-renew-notice/workflows/SSO%20UI%20Renew%20Notice/badge.svg)

Send periodic notifications regarding the expiration date of your Universitas Indonesia account's password to your telegram account.


### Make it your own

Clone this repo, create a new github repo, and enter the following secrets to your github repo secrets

```
// Your Universitas Indonesia account username and password

SSO_USERNAME
SSO_PASSWORD
```

```
// Telegram chat id and your telegram bot token
// For further information, read README of the repo below
// https://github.com/appleboy/telegram-action

TELEGRAM_TO
TELEGRAM_TOKEM
```

```
// Your name and your github email

email
name
```

### Run sso-login script locally

Install everything that needed to run the script
```
pip install -r requirements.txt
```

Run the sso-login script
```
python sso-login.py
```


## Built With

* [Github Actions](https://github.com/features/actions) - Github actions
* [Python](https://www.python.org/) - Python programming language
* [Pip](https://pip.pypa.io/en/stable/) - Python dependencies manager
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium
* [Django Environ](https://github.com/joke2k/django-environ) - Read secrets and env
* [setup-chromedriver](https://github.com/nanasess/setup-chromedriver) - Github action to setup chrome driver
* [telegram-action](https://github.com/appleboy/telegram-action) - Github action to send telegram message


## Authors

* **Arga Ghulam Ahmad** - *Initial work* - [@argaghulamahmad/sso-ui-renew-notice](https://github.com/argaghulamahmad/sso-ui-renew-notice)