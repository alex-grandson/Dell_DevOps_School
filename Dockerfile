FROM python:3.8

# building speed better
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /usr/src/dell_devops/weather_app
WORKDIR /usr/src/dell_devops/weather_app

COPY . /usr/src/dell_devops/weather_app

EXPOSE 5000

CMD ["python", "app.py"]