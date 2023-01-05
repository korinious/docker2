FROM python:3-alpine3.15

WORKDIR /docker2

COPY . /docker2

RUN pip install -r requirements.txt

EXPOSE 3000

CMD python ./docker2.py