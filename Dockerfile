from python:3.5

RUN pip3 install psycopg2
RUN pip install psycopg2-binary

ENV  PYTHONUNBUFFERED=1

WORKDIR /event-server

COPY . /event-server

CMD python3 /event-server/server.py
