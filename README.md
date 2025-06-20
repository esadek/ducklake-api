# DuckLake API

[![CI Status](https://img.shields.io/github/actions/workflow/status/esadek/ducklake-api/ci.yml)](https://github.com/esadek/ducklake-api/actions/workflows/ci.yml)
[![Supported Python Versions](https://img.shields.io/badge/python-3.10+-blue)](pyproject.toml)
[![License](https://img.shields.io/github/license/esadek/ducklake-api)](LICENSE)
[![Powered by FastAPI](https://img.shields.io/badge/powered_by-FastAPI-009688)](https://github.com/fastapi/fastapi)

A simple REST API for DuckLake

## Installation

Clone repository and change directory:

```bash
git clone https://github.com/esadek/ducklake-api.git
cd ducklake-api
```

## Usage

Run the server:

```bash
uv run src/ducklake_api/main.py
```

Then open http://127.0.0.1:8000 in your browser.

## Documentation

Three endpoints are available for API documentation.

- `GET /` - [Scalar](https://github.com/scalar/scalar) (recommended)
- `GET /docs` - [Swagger UI](https://github.com/swagger-api/swagger-ui)
- `GET /redoc` - [Redoc](https://github.com/Redocly/redoc)
