FROM python:3.12-alpine
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /get-by/backend

COPY requirements.txt ./

# Build psycopg2-binary from source -- add required required dependencies
RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps
# RUN useradd getby
# USER getby

COPY . /get-by/backend/

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD [ "python", "manage.py", "createsuperuser" ]