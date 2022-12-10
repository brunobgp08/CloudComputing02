FROM python:3.9

# Instalando dependências (bibliotecas)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Rodando a aplicação
COPY main.py .
CMD ["python", "main.py"]
