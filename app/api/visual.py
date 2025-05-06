import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, List
from app.services.ai_visual_service import generate_visual, save_visual, upload_image

router = APIRouter()

class VisualRequest(BaseModel):
    script: str = Field(..., min_length=1)
    type: Literal["image", "video"]
    style: str = Field(..., min_length=1)
    resolution: str = Field(default="1024x1024")

class VisualItem(BaseModel):
    visual_id: str
    visual_url: str
    type: str
    style: str

class VisualResponse(BaseModel):
    visuals: List[VisualItem]

@router.post("/visuals", response_model=VisualResponse)
async def create_visual(request: VisualRequest):
    try:
        responses = generate_visual(
            script=request.script,
            type=request.type,
            style=request.style,
            resolution=request.resolution
        )

        visual_object_list = save_visual(responses=responses, resolution=request.resolution)
        response_urls = upload_image(visual_object_list=visual_object_list)

        visual_items = []
        
        for obj, url in zip(visual_object_list, response_urls):
            visual_items.append(
                VisualItem(
                    visual_id=os.path.splitext(obj["visual_name"])[0],
                    visual_url=url,
                    type=request.type,
                    style=request.style,
                )
            )

        return VisualResponse(visuals=visual_items)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Visual generation failed: {str(e)}")