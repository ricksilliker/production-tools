FROM python:3.9

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./app.py /
COPY ./api/. /api
COPY ./definitions/. /definitions

ENTRYPOINT ["python", "app.py"]
