FROM python:3.8

WORKDIR /docker2

ADD . /docker2

RUN pip install --trusted-host pypi.python.org Flask Redis

EXPOSE 80
CMD ["python", "docker2.py"]