# install python in the container
FROM python:latest
# copy the local requirements.txt file to the
# /app/requirements.txt in the container
# (the /app dir will be created)
COPY ./requirements.txt /app/requirements.txt
# install the packages from the requirements.txt file in the container
RUN pip install -r /app/requirements.txt

# copy the local app/ folder to the /app fodler in the container
COPY app/ /app
# set the working directory in the container to be the /app
WORKDIR /app

CMD ["python3", "main.py"]
