FROM python:3.9

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app.py /
COPY ./api/. /api
COPY swagger.yaml /

CMD ['python', 'app.py']
