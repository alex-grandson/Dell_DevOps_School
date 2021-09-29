FROM python:3.8

RUN mkdir -p /usr/src/dell_devops/weather_app
WORKDIR /usr/src/dell_devops/weather_app

COPY . /usr/src/dell_devops/weather_app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]