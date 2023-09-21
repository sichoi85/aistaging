from python:3.11.1
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--reload"] 

#port 8000 bydefault