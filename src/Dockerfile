FROM python


#================================ Python ================================
WORKDIR /src
ADD analyser.py analyser.py
ADD client_http/client.py client.py


CMD ["python3", "./analyser.py"]
#CMD  ["python3", "client.py", "127.0.0.1", "80"]