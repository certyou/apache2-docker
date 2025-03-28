FROM python
FROM httpd


#================================ Python ================================
# script
ADD /src/hello_world.py hello_world.py
ADD /src/client_http/client.py client.py

#CMD ["python3", "./hello_world.py"]
CMD  ["python3", "client.py", "127.0.0.1", "80"]