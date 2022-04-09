FROM python:3.10.4-bullseye as build

# Install dependencies:
WORKDIR /tmp/
RUN pip install --no-cache-dir poetry==1.1.13
COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && poetry install --no-root --no-dev

FROM python:3.10.4-slim-bullseye as runtime

WORKDIR /app/
RUN useradd appuser

# Copy dependencies from previous stage:
ENV PATH=/opt/.venv/bin:$PATH
COPY --from=build /tmp/.venv /opt/.venv

# Copy the app file(s):
COPY app/* ./

USER appuser
CMD ["python3", "main.py"]
