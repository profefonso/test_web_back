FROM python:3.6.7-jessie

WORKDIR /
COPY . /app

EXPOSE 8000

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/manage.py", "migrate"]

CMD ["python", "/app/manage.py", "loaddata", "/app/fixtures/fix_district.json"]

CMD ["python", "/app/manage.py", "loaddata", "/app/fixtures/fix_municipalitys.json"]

CMD ["python", "/app/manage.py", "loaddata", "/app/fixtures/fix_tags.json"]

CMD ["python", "/app/manage.py", "loaddata", "/app/fixtures/fix_topic.json"]

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]