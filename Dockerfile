FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt -i http://pypi.qima-inc.com/youzan/dev/+simple/ --trusted-host pypi.qima-inc.com
ADD . /code/