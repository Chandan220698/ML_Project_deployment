FROM python:3.7
COPY . /app
WORKDIR /app
ADD requirements.txt ./
WORKDIR /app
RUN pip install -r requirements.txt --no-deps -t python/lib/python3.6/site-packages/
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
