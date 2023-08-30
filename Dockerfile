# Use the specified Python version.
FROM python:3.10-slim-bullseye
LABEL description="Events api"

# Install system dependencies.
RUN apt-get update && \
    apt-get -y install libpq-dev gcc curl procps net-tools tini && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Gunicorn for production deployments.
RUN pip install gunicorn

# Install poetry.
ENV POETRY_HOME=/tmp/poetry
RUN curl -sSL https://install.python-poetry.org/ | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1

# Create a working directory.
WORKDIR /app

# First, copy only the dependencies specification to leverage Docker cache.
COPY ./pyproject.toml ./poetry.lock /app/

# Configure poetry to install the packages globally.
RUN poetry config virtualenvs.create false

# Install project dependencies.
# This is split into a separate step so that dependencies can be cached separately from the application code.
RUN if [ "$ENVIRONMENT" = "production" ]; then \
    poetry install --no-dev --no-interaction --no-ansi; \
else \
    poetry install --no-interaction --no-ansi; \
fi

# Copy the rest of the application code.
COPY . /app/

# Expose the port the app runs on.
EXPOSE 8000
