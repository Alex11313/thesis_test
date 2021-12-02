FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY thesis_test ./thesis_test

WORKDIR /app/

EXPOSE 8000
CMD ["gunicorn", "thesis_test.wsgi", "-w", "4", "-b 0.0.0.0:8000", "--env", "DJANGO_SETTINGS_MODULE=thesis_test.settings", "--pythonpath=/usr/local/lib/python3.8/site-packages/", "--preload"]
