From python:alpine3.10
WORKDIR /app
Copy . /app
Run pip install -r requirements.txt
Expose 5000
CMD python ./launch.py
