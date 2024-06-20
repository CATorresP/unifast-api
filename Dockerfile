FROM python:3.12-slim

WORKDIR /app


COPY . .
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    unixodbc-dev \
    build-essential \
    curl \
    gnupg

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17


EXPOSE 5000


CMD ["uvicorn", "main:app", "--host", "app01", "--port", "5000"]