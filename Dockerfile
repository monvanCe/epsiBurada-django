FROM python:3.11

WORKDIR /epsiburada

COPY requirements.txt /epsiburada/
RUN pip install -r requirements.txt

COPY . /epsiburada/

RUN python manage.py collectstatic --noinput

