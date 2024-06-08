FROM python:3.9

RUN apt-get update && apt-get install -y nano

WORKDIR /code

COPY requirements.txt /code/requirements.txt

RUN pip install --no-cache --upgrade -r requirements.txt

COPY . /code

EXPOSE 80

CMD ["uvicorn", "run:app", "--host", "0.0.0.0", "--port", "80"]
