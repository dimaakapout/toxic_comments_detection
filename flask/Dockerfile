FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app/

COPY . /usr/src/app
RUN pip install flask
RUN pip install numpy
RUN pip install sklearn
RUN pip install gunicorn
EXPOSE 5002

# CMD ["python", "app.py"]