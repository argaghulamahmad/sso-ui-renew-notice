# SSO UI Password Renew Notice


![SSO UI Renew Notice](https://github.com/argaghulamahmad/sso-ui-renew-notice/workflows/SSO%20UI%20Renew%20Notice/badge.svg)


![Screenshoot at telegram](md-assets/sso-ui-renew-notice-bot-telegram.png)


Send periodic (daily) notifications regarding the expiration date of your Universitas Indonesia account's password to your telegram bot.
Built with python, selenium, chromedriver, telegram bot api, cron, and github action.

### Why?
#### Telegram?
The easiest instant messaging app bot to configure
#### Build this bot?
Prevents University of Indonesia student email accounts from expiring because they forgot to change their password.
#### Github Action?
- Github action provide pipeline that free to use without limit as long the repo visiblity is public
- Can triggered with cron (linux time scheduler)
#### Learning purpose
- Learn how to utilize github action
- Discover interesting github action that develop by community
- Develop telegram bot

### Make it your own
#### Clone this repo

```bash
git clone https://github.com/argaghulamahmad/sso-ui-renew-notice.git
```

#### [Create a new repo on your github account.](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-new-repository)
#### [Create your own telegram bot.](https://core.telegram.org/bots)
#### [Enter the following secrets to your github repo secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets)

```
// Your Universitas Indonesia account username and password

SSO_USERNAME // without @ui.ac.id
SSO_PASSWORD // your email account's password
```

```
// Telegram chat id and your telegram bot token
// For further information, read README of the repo below
// https://github.com/appleboy/telegram-action

TELEGRAM_TO     // chat id with bot
TELEGRAM_TOKEN  // telegram api token
```

```
// Your name and your github email

email           // your github email
name            // your name
```

#### Push to your own repo
Remove the current remote origin and add your repo as remote origin
```
git remote remove origin
git remote add origin <your-github-repo>
```
Push to your own repo
```
git push origin master
```

## Built With

* [Github Actions](https://github.com/features/actions) - Github actions
* [Python](https://www.python.org/) - Python programming language
* [Pip](https://pip.pypa.io/en/stable/) - Python dependencies manager
* [Selenium](https://github.com/SeleniumHQ/selenium) - Selenium
* [Django Environ](https://github.com/joke2k/django-environ) - Read secrets and env
* [setup-chromedriver](https://github.com/nanasess/setup-chromedriver) - Github action to setup chrome driver
* [telegram-action](https://github.com/appleboy/telegram-action) - Github action to send telegram message

### How-to? Run sso-login script locally

Install everything that needed to run the script
```
pip install -r requirements.txt
```

Run the sso-login script
```
python sso-login.py
```

## References

* https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow
* https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions
* https://help.github.com/en/actions/configuring-and-managing-workflows/using-environment-variables
* https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets

## Authors

* **Arga Ghulam Ahmad** - *Initial work* - [@argaghulamahmad/sso-ui-renew-notice](https://github.com/argaghulamahmad/sso-ui-renew-notice)