ARG venv="/mnt/.venv"

FROM python:3.9-buster AS builder

ENV PIP_DISABLE_PIP_VERSION_CHECK=true

WORKDIR /mnt

COPY pyproject.toml .
COPY poetry.lock .

RUN pip3 install poetry

RUN poetry config virtualenvs.create true --local
RUN poetry config virtualenvs.in-project true --local

RUN poetry install --no-dev

FROM python:3.9-slim-buster AS runtime
ARG venv
ENV PATH="${venv}/bin/:$PATH"

WORKDIR /mnt

COPY --from=builder "${venv}" "${venv}"
COPY . .

CMD ["uvicorn",  "main:app", "--host", "0.0.0.0"]
