FROM ubuntu:latest


#================================ Python ================================
# local environnement
COPY .venv/ /.venv/
# script
COPY app/ /app/

#CMD  ["client.py", "127.0.0.1", "80"]
CMD ["hello_world.py"]

# apache
WORKDIR /

#RUN sudo apt install apache2