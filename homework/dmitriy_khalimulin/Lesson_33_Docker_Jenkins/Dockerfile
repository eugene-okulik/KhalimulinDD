FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update && apt-get install -y python3 python3-pip wget
RUN pip3 install --upgrade pip --break-system-packages && pip3 install --break-system-packages pytest allure-pytest requests Faker python-dotenv selenium
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
USER jenkins