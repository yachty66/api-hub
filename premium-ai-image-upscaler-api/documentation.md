# Premium AI Image Upscaler API

Premium AI Image Upscaler API transforms your images into high-quality, enhanced versions with improved resolution and clarity:

| Before | After |
|--------|-------|
| ![Before Image](https://storage.googleapis.com/apihub85/0_1.webp) | ![After Image](https://storage.googleapis.com/apihub85/upscaled_image.png) |

## Getting Started

To begin using the Premium AI Image Upscaler API, follow these steps:

1. **Subscribe to a plan**: Visit our [Pricing page](https://rapidapi.com/arxivgpt-arxivgpt-default/api/premium-ai-image-upscaler-api1/pricing) on RapidAPI and choose a subscription plan that fits your needs.

2. **Make your first API call**: Use the RapidAPI Playground to test the endpoint. Simply provide an image URL and an enhancement prompt to see the API in action.

3. **Integrate into your application**: Use the provided code snippets to integrate the API into your project.

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

| Parameter  | Type   | Required | Description                                    |
|------------|--------|----------|------------------------------------------------|
| image_url  | string | Yes      | URL of the image to process                    |
| prompt     | string | Yes      | Prompt to guide the AI enhancement (e.g., "UHD 4k vogue style") |

#### Response

Returns a JSON object containing:
- `status`: Success status of the request
- `image`: Base64-encoded enhanced image
- `format`: Image format (typically "png")

#### Example Response

```json
{
    "status": "success",
    "image": "base64_encoded_image_data",
    "format": "png"
}
```

#### Code Example

This code example will take the turn the result into a .png file named upscaled_image.png.

```python
import requests
import base64

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

image_data = base64.b64decode(data["image"])
with open("upscaled_image.png", "wb") as f:
    f.write(image_data)
print("Image saved successfully")
```

## Best practices

The prompt is required for the model, and the more the prompt describes the input image, the better the result. If you want to use this API in an automated pipeline, you can either try a strategy where you use a vision model to create a good prompt, or you can use a general prompt; the model will still output a reasonable result.

## Support

In case you are facing any issues, please send a message with the issue to maxhager28@gmail.com. A response will come within 24 hours, guaranteed.