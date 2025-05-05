FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app

# Enable bytecode compilation and set link mode to copy
# ENV UV_COMPILE_BYTECODE=1 \
#     UV_LINK_MODE=copy

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies without installing the project itself
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copy the rest of the application code
COPY . .

# Install the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Set the default command to run the application
CMD ["sh", "-c", "cp scripts/jobs/github/get-issues-and-push-to-todoist.sh . && sh get-issues-and-push-to-todoist.sh"]