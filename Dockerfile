FROM python:3.9-buster
COPY . app
EXPOSE 5000
WORKDIR app
RUN pip install -r requirements.txt
CMD python app.py