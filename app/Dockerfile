FROM alpine:latest

RUN apk add --no-cache python3 \
    py3-pip \
     && pip install flask bs4 requests

EXPOSE 5000

COPY ./app /app

ADD BFBJVDYGDBJH_flag.txt /

ENTRYPOINT [ "python3" ]

CMD [ "/app/app.py" ]
