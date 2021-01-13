FROM python:3.7
ENV PYTHONUNBUFFERED=1
ARG REQUIREMENTS_FILE="base"
WORKDIR /code
COPY requirements /code
RUN pip install -r /code/$REQUIREMENTS_FILE.txt
COPY source /code
RUN python /code/manage.py collectstatic --noinput
EXPOSE 8000