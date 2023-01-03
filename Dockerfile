FROM python:3.10.8

WORKDIR /Index

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /Index

ENTRYPOINT ["streamlit", "run"]

CMD ["Index.py"]