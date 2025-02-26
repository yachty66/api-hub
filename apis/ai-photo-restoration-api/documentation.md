# Premium AI Image Upscaler API

Premium AI Image Upscaler API transforms your images into high-quality, enhanced versions with improved resolution and clarity:

| Before                                                            | After                                                                      |
| ----------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ![Before Image](https://storage.googleapis.com/apihub85/0_1.webp) | ![After Image](https://storage.googleapis.com/apihub85/upscaled_image.png) |

## Getting Started

To begin using the Premium AI Image Upscaler API, follow these steps:

1. **Subscribe to a plan**: Visit our [Pricing page](https://rapidapi.com/arxivgpt-arxivgpt-default/api/premium-ai-image-upscaler-api1/pricing) on RapidAPI and choose a subscription plan that fits your needs.

2. **Make your first API call**: Use the [code example below](#code-example) to test the endpoint. Simply provide an image URL and an enhancement prompt, or use the example URL from the RapidAPI page to see the API in action.

> **Note**: On your first request, the API server may need to cold start, which can take up to 3 minutes. All subsequent requests will be significantly faster. This is normal behavior and only affects the very first request after a period of inactivity. If you need the server to be permanently available without cold starts, please reach out to support@apilexica.com.

## Authentication

Authentication is handled through RapidAPI. Include these headers in your requests:

- `X-RapidAPI-Key`: Your RapidAPI key
- `X-RapidAPI-Host`: "premium-ai-image-upscaler-api1.p.rapidapi.com"

## Endpoint

### Upscale Image

```
GET /upscale
```

Enhances and upscales an image using AI technology.

#### Parameters

| Parameter | Type   | Required | Description                                                     |
| --------- | ------ | -------- | --------------------------------------------------------------- |
| image_url | string | Yes      | URL of the image to process                                     |
| prompt    | string | Yes      | Prompt to guide the AI enhancement (e.g., "UHD 4k vogue style") |

#### Response

Returns a JSON object containing:

- `status`: Success status of the request
- `url`: Direct URL to the enhanced image

#### Example Response

```json
{
  "status": "success",
  "url": "https://api-lexica.s3.amazonaws.com/premium-ai-image-upscaler-api/97ed1614-7986-424f-ad9f-5a4335408e0e.png"
}
```

#### Code Example

This code example (you still need to insert your personal details, like the image URL and your API key) will turn the result into a .png file named upscaled_image.png.

```python
import requests

url = "https://premium-ai-image-upscaler-api1.p.rapidapi.com/upscale"

querystring = {
    "prompt": "UHD 4k",
    "image_url": "YOUR_IMAGE_URL"
}

headers = {
    "x-rapidapi-key": "YOUR_API_KEY",
    "x-rapidapi-host": "premium-ai-image-upscaler-api1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
```

## Best practices

The prompt is required for the model, and the more the prompt describes the input image, the better the result. If you want to use this API in an automated pipeline, you can either try a strategy where you use a vision model to create a good prompt, or you can use a general prompt; the model will still output a reasonable result.

## Support

In case you are facing any issues, please send a message with the issue to support@apilexica.com. A response will come within 24 hours, guaranteed.
