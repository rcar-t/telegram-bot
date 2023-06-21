FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

CMD [ "python", "main.py" ]