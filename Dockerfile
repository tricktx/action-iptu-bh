FROM ubutu-lastest

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip


# Path: requirements.txt

COPY requirements.txt /requirements.txt

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT ["python3", "/main.py"]