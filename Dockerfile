FROM python:3.9.5

WORKDIR /netflix

COPY . /netflix

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "./entrypoint.sh" ]