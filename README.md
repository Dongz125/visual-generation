# Visual Generation API

A FastAPI-based service that generates visual content (images/videos) based on text descriptions using AI.

## Features

- Generate images and videos from text descriptions
- Support for different artistic styles
- Customizable resolution for generated content
- Cloud storage integration for generated visuals
- RESTful API endpoints

## Prerequisites

- Python 3.11.0 or higher
- pip (Python package manager)
- Cloudinary account (for image storage)
- Google AI API credentials

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd visual-generation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```env
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
GOOGLE_API_KEY=your_google_api_key
```

## Running the Application

### Local Development
```bash
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`

### Production
```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## API Documentation

### Health Check
```http
GET /health
```
Response:
```json
{
    "status": "healthy"
}
```

### Generate Visual Content
```http
POST /visuals
```

Request Body:
```json
{
    "script": "Black holes are regions of spacetime where gravity is so strong that nothing, including light, can escape from them. At the center of a black hole lies a singularity, a point where the laws of physics as we know them break down. The boundary of a black hole is called the event horizon, beyond which events cannot affect an outside observer.",
    "type": "image",
    "style": "realistic",
    "resolution": "1024x1024"
}
```

Parameters:
- `script` (string, required): Description of the visual content to generate
- `type` (string, required): Type of content ("image" or "video")
- `style` (string, required): Artistic style for the generation
- `resolution` (string, optional): Resolution of the output (default: "1024x1024")

Response:
```json
{
  "visuals": [
    {
      "visual_id": "66b2dd4b-ffbe-4567-b52d-28b2b7f33353",
      "visual_url": "https://res.cloudinary.com/dddhsnmiw/image/upload/v1746524697/66b2dd4b-ffbe-4567-b52d-28b2b7f33353.png",
      "type": "image",
      "style": "realistic"
    },
    {
      "visual_id": "21a2b14a-8877-4bf2-9599-cde04fe77ccd",
      "visual_url": "https://res.cloudinary.com/dddhsnmiw/image/upload/v1746524699/21a2b14a-8877-4bf2-9599-cde04fe77ccd.png",
      "type": "image",
      "style": "realistic"
    },
    {
      "visual_id": "492786bc-fcc2-4376-9b0b-1878bf599752",
      "visual_url": "https://res.cloudinary.com/dddhsnmiw/image/upload/v1746524701/492786bc-fcc2-4376-9b0b-1878bf599752.png",
      "type": "image",
      "style": "realistic"
    }
  ]
}
```

## Testing with Thunder Client

1. Install Thunder Client extension in VS Code
2. Create new requests:

### Health Check
- Method: GET
- URL: `http://localhost:8000/health`

### Generate Visual
- Method: POST
- URL: `http://localhost:8000/visuals`
- Headers: 
  ```
  Content-Type: application/json
  ```
- Body:
  ```json
  {
      "script": "A beautiful sunset over mountains",
      "type": "image",
      "style": "realistic",
      "resolution": "1024x1024"
  }
  ```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Successful request
- 400: Bad request (invalid parameters)
- 500: Internal server error

Error response format:
```json
{
    "detail": "Error message description"
}
```

## Deployment

The application is configured for deployment on Railway:
1. Push your code to GitHub
2. Create a new project on Railway
3. Connect your GitHub repository
4. Set up environment variables in Railway dashboard
5. Deploy!

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here]

## Support

For support, please [create an issue](your-repository-issues-url) in the repository.
