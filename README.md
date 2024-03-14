# Spam Detection API

Welcome to the Spam Detection API! This API allows you to check if a given text is spam or not. It's easy to use and can be integrated into your own applications or services.

## Features

- Spam detection: Send text to the API and get a prediction indicating whether the text is considered spam or not.
- Customization: Ability to provide additional parameters to improve the prediction.

## Usage

### Accessing the API

The API is accessible via a URL. Here's the base URL: "it's coming"

### Endpoint `/detect-spam`

This endpoint is used to detect whether a given text is spam or not. Here's how to use it:

- **URL:** `/detect-spam`
- **HTTP Method:** POST
- **Request Parameters:**
  - `text`: Text to analyze (required)
  - `extra` (optional): Additional parameter to improve the prediction

Example HTTP request:

```http
POST /detect-spam HTTP/1.1
Host: 
Content-Type: application/json

{
  "text": "Click here to win a million dollars!"
}

