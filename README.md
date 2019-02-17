# test_web_back

# Crate user and data base in postgresql

CREATE USER test_user WITH password 'T3sT';

CREATE DATABASE test_db WITH OWNER test_user;

# Run Project

pip install -r requirements.txt

python manage.py migrate

python manage.py loaddata fixtures/fix_district.json

python manage.py loaddata fixtures/fix_municipalitys.json

python manage.py loaddata fixtures/fix_tags.json 

python manage.py loaddata fixtures/fix_topic.json
