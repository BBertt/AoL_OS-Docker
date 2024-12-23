FROM python:3.10.2-slim
# specify the base image to use for the docker container.

WORKDIR /app
# to state that the working directory is the app.

COPY . /app
# copies all the directory into the /app of the docker container.

RUN python -m pip install -r requirements.txt
# run to install the dependencies.

EXPOSE 80
# make app listen to port 80 for incoming traffic.

CMD [ "python" , "app.py" ]
# default command that runs when the container starts.