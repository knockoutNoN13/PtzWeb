FROM alpine:latest

RUN apk add --no-cache python3 \
    py3-pip \
     && pip install flask bs4 requests

EXPOSE 8080

COPY ./ /app

ENTRYPOINT [ "python3" ]

CMD [ "/app/app.py" ]
