FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq
RUN apt-get install texlive-latex-recommended -y
RUN apt-get install texlive-lang-cyrillic -y
RUN apt install python3-pip -y

COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt

RUN chmod +x /app/run.sh
# ENTRYPOINT ["/app/run.sh"]
