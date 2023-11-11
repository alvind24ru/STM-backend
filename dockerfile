FROM ubuntu

WORKDIR /app

RUN apt update -y && apt install git python3 pip -y && git clone https://github.com/alvind24ru/STM-backend.git && cd STM-backend && pip install -r requirements.txt

EXPOSE 5000

CMD git pull
CMD python3 STM-backend/main.py