FROM python:3.10.4

WORKDIR /app/
RUN useradd appuser

# Install dependencies:
RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Copy the app file(s):
COPY main.py ./

USER appuser
CMD ["python3", "main.py"]
