FROM python:3.10-slim
RUN apt-get update
RUN apt-get install -y virtualenv
#
ARG WORK=/work
RUN mkdir $WORK
WORKDIR $WORK
RUN virtualenv venv
RUN . venv/bin/activate
#
RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt
#
COPY src/ .
ENTRYPOINT ["python", "/work/main.py"]