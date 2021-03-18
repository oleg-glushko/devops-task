FROM python:3.8-alpine

ENV FLASK_PORT=
EXPOSE 5000

WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
COPY app.py /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
