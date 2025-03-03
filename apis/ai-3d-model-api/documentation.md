# AI Photo Restoration API

Transform your degraded images into high-quality, restored versions using AI technology:

| Before                                                            | After                                                                      |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ![Before Image](https://api-lexica.s3.us-east-1.amazonaws.com/examples/0014.jpg) | ![After Image](https://api-lexica.s3.amazonaws.com/ai-photo-restoration-api/baa747c8-e5d3-43b3-b436-d4ff7ed8bdee.png) |

## Getting Started

To begin using the AI Photo Restoration API, follow these steps:

1. **Subscribe to a plan**: Visit our [Pricing page](https://rapidapi.com/arxivgpt-arxivgpt-default/api/ai-photo-restoration-api/pricing) on RapidAPI and choose a subscription plan that fits your needs.

2. **Make your first API call**: Use the [code example below](#code-example) to test the endpoint. Simply provide an image URL to restore your image to high quality.

> **Note**: On your first request, the API server may need to cold start, which can take a little bit longer. All subsequent requests will be significantly faster. This is normal behavior and only affects the very first request after a period of inactivity. If you need the server to be permanently available without cold starts, please reach out to support@apilexica.com.

## Authentication

Authentication is handled through RapidAPI. Include these headers in your requests:

- `X-RapidAPI-Key`: Your RapidAPI key
- `X-RapidAPI-Host`: "ai-photo-restoration-api.p.rapidapi.com"

## Endpoint

### Restore Image

```
GET /restore
```

Restores and enhances images using advanced AI technology.

#### Parameters

| Parameter | Type   | Required | Description                 |
| --------- | ------ | -------- | --------------------------- |
| image_url | string | Yes      | URL of the image to restore |

#### Response

Returns a JSON object containing:

- `status`: Success status of the request
- `url`: Direct URL to the restored image

#### Example Response

```json
{
  "status": "success",
  "url": "https://api-lexica.s3.amazonaws.com/ai-photo-restoration-api/baa747c8-e5d3-43b3-b436-d4ff7ed8bdee.png"
}
```

#### Code Example

```python
import requests

url = "https://ai-photo-restoration-api.p.rapidapi.com/restore"

querystring = {
    "image_url": "YOUR_IMAGE_URL"
}

headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "ai-photo-restoration-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
```

## Support

In case you are facing any issues, please send a message with the issue to support@apilexica.com. A response will come within 24 hours, guaranteed.