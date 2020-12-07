FROM python:3.7
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements /code
RUN pip install -r /code/base.txt
COPY source /code
EXPOSE 8000