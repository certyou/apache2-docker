FROM python


#================================ Python ================================
# script
ADD /app/hello_world.py hello_world.py
ADD /app/client_http/client.py client.py

CMD  ["python3", "client.py", "127.0.0.1", "80"]
#CMD ["python3", "./hello_world.py"]