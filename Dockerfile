FROM python:3.12

RUN pip install --upgrade pip && pip install pipenv

ENV SOURCE_DIR=/app
ENV BUILD_DIR=/home/app/core/

RUN mkdir -p ${BUILD_DIR}

WORKDIR ${BUILD_DIR}

COPY ${SOURCE_DIR} ${BUILD_DIR}

RUN apt-get update && apt-get install -y postgresql-client

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh


RUN pipenv install --dev



ENTRYPOINT ["/entrypoint.sh"]

CMD ["pipenv", "run", "todo_core/manage.py"]