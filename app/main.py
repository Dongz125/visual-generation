from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.visual import router as visual_router

app = FastAPI(title="Visual Generation Service")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(visual_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
