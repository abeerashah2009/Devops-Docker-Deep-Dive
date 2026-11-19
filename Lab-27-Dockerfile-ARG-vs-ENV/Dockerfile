FROM python:3.12-slim

ARG APP_VERSION=1.0.0

ENV APP_ENV=production
ENV APP_VERSION_BUILT=$APP_VERSION

RUN echo "Building version $APP_VERSION"

WORKDIR /app
COPY . /app

CMD ["python", "app.py"]
