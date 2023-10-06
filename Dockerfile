FROM python:3.11.6-alpine3.18
WORKDIR /app
COPY . .
EXPOSE 8000
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
CMD ["python", "main.py"]