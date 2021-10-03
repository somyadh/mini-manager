# syntax=docker/dockerfile:1

FROM python:3.8-slim

WORKDIR /app 
# We copy just the requirements.txt first to leverage Docker cache
COPY Pipfile* .

RUN pip install pipenv && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  pipenv install --deploy --system && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y && \
  pip uninstall pipenv -y

COPY . .
ENV FLASK_APP app.py
EXPOSE 5000

CMD [ "flask", "run", "-h", "0.0.0.0"]