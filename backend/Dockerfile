FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV="docker"
EXPOSE 5000

# put this in docker-compose for now
#HEALTHCHECK CMD curl --fail http://localhost:5000/ || exit 1

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

#CMD python3 app.py