FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app

COPY pyproject.toml ./

# Copy the rest of the application code
COPY . .

# Install the project
RUN uv sync

CMD ["uv", "run", "main.py"]