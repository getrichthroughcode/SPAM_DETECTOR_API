FROM python:3.12


WORKDIR /app

COPY pyproject.toml poetry.lock requirements.txt ./

RUN pip install poetry


RUN poetry install --no-dev

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "python", "src/app.py"]