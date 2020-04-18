#publicly available docker image "python" on docker hub will be pulled

FROM python

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# set display port to avoid crash
ENV DISPLAY=:99

# add script and requirements
ADD ./sso_ui/sso-login.py /
ADD requirements.txt /
ADD sso-ui-renew-notice.sh /

# install requirements
RUN pip install -r requirements.txt

# run bash script
RUN chmod +x sso-ui-renew-notice.sh
CMD [ "./sso-ui-renew-notice.sh" ]
