FROM python:3.7-stretch

WORKDIR /fastapi

COPY ./requirements.txt /fastapi/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /fastapi

CMD ["gunicorn", "main:app" ,"--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000"]