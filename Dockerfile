FROM python:3.12 AS builder

WORKDIR /build

COPY Pipfile /build/

RUN pip install --upgrade pip && \
    pip install pipenv 

ENV PIPENV_VENV_IN_PROJECT=1    

RUN pipenv install 

FROM python:3.12-slim AS final

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 

RUN mkdir /app

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev

COPY --from=builder /build/.venv /app/.venv

COPY todo_core /app/todo_core

COPY .env /app/

COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["sh", "/app/entrypoint.sh"]