FROM python:3.10-slim

WORKDIR /project

COPY alembic /project/alembic
COPY app /project/app
COPY patched.py /project/patched.py
COPY poetry.toml /project/poetry.toml

RUN pip install -U pip setuptools
RUN pip install poetry
RUN poetry install

CMD gunicorn --worker-class gevent \
  --workers $WORKERS \
  --bind 0.0.0.0:$PORT_APP \ 
  patched:app

