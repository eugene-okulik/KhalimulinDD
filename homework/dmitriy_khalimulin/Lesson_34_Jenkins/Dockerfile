# Используем базовый образ Jenkins с JDK 17
FROM jenkins/jenkins:lts-jdk17

# Переходим на пользователя root для выполнения команд установки
USER root

# Обновляем систему и устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv wget

# Добавляем ключ для Google Chrome и устанавливаем Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# Возвращаемся к пользователю Jenkins
USER jenkins