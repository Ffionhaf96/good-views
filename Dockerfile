FROM python:3.12.2-alpine

WORKDIR /good-views

COPY ./app /good-views/app
COPY requirements.txt /good-views/
COPY run.py /good-views/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=run.py

CMD ["gunicorn", "-w", "4", "-b", ":5000", "--reload", "--log-level", "debug", "run:app"]
