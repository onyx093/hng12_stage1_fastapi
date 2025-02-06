# FastAPI Public API

## Description

A simple FastAPI-based public API returning an email, current UTC time, and GitHub repository URL.

## Endpoint

**GET** [https://hng12stage1fastapi.vercel.app](https://hng12stage1fastapi.vercel.app/)

### Response Example (200 OK)

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}
```

## Setup Instructions

1. Clone the repo:

```
git clone https://github.com/onyx093/hng12_stage1_fastapi
cd fastapi-public-api
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the API locally:

```
uvicorn main:app --reload
```

### Hiring Links

[Hire Python Developers](https://hng.tech/hire/python-developers)
[Hire C# Developers](https://hng.tech/hire/csharp-developers)
[Hire Golang Developers](https://hng.tech/hire/golang-developers)
[Hire PHP Developers](https://hng.tech/hire/php-developers)
[Hire Java Developers](https://hng.tech/hire/java-developers)
[Hire Node.js Developers](https://hng.tech/hire/nodejs-developers)
