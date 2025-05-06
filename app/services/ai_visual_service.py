import os
import uuid
import spacy
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from app.config.settings import GEMINI_API_KEY, STATIC_DIR, cloudinary
import cloudinary.uploader

client = genai.Client(api_key=GEMINI_API_KEY)

def generate_visual(script: str, type: str, style: str, resolution: str) -> str:
    '''
    params: 
        script: str
        type: str
        style: str
        resolution: str
    ----------------------------
    return:
        response: object
    '''
    try:
        # separate script
        if type == "image":
            try:
                nlp = spacy.load("en_core_web_sm")
            except OSError:
                spacy.cli.download("en_core_web_sm")
                nlp = spacy.load("en_core_web_sm")
                
            doc = nlp(script)
            descriptions = [sent.text for sent in doc.sents]

            responses = []

            for description in descriptions:
                response = client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=f"{description}. Create a picture of it with no word in the picture.",
                    config=types.GenerateContentConfig(
                        response_modalities=['TEXT', 'IMAGE']
                    )
                )

                responses.append(response)

        return responses
       
    except Exception as e:
        print(f"Error in generate_visual: {str(e)}")
        raise e  # Re-raise the exception
    
def save_visual(responses, resolution: str):
    '''
    param: 
        response: object
    
    returns:
        visual_path: str
        visual_name: str
    '''
    if not os.path.exists(STATIC_DIR):
        try:
            os.makedirs(STATIC_DIR)
        except Exception as e:
            print(f"Error creating STATIC_DIR: {str(e)}")
            raise e

    try:
        visual_object_list = []

        for response in responses:
            visual_name = f"{uuid.uuid4()}.png" # Tạo UUID ngẫu nhiên
            visual_path = os.path.join(STATIC_DIR, visual_name)

            for part in response.candidates[0].content.parts:
                if part.inline_data is not None:
                    image = Image.open(BytesIO((part.inline_data.data)))
                    # width, height = map(int, resolution.split('x'))
                    #image = image.resize((width, height), Image.Resampling.LANCZOS)
                    image.save(visual_path)
                    #image.show()

            visual_object = {
                "visual_name": visual_name,
                "visual_path": visual_path
            }

            visual_object_list.append(visual_object)

        return visual_object_list

    except Exception as e:
        print(f"Error in save_visual: {str(e)}")
        raise e
    
def upload_image(visual_object_list):
    try:
        response_urls = []

        for visual_object in visual_object_list:
            name = os.path.splitext(visual_object["visual_name"])[0]
            response = cloudinary.uploader.upload(visual_object["visual_path"], public_id=name)
            response_urls.append(response['secure_url'])

        return response_urls

    except Exception as e:
        print(f"Error in upload_visual: {str(e)}")
        raise e