FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt-get update && apt-get -y install vim && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "sleep", "3600" ]


