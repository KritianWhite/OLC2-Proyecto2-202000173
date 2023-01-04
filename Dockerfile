FROM python:3.10.8

WORKDIR /pythonDocker

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /Index

CMD ["streamlit", "run", "Index.py"]
