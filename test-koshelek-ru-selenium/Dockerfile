FROM python:3.10
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt


RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /etc/apk/cache && rm -rf /var/lib/apt/lists/*

WORKDIR /code
COPY . .

#CMD ["pytest", "-v", "-m checkbox", "tests/test_page.py", "--alluredir=allure-results"]
