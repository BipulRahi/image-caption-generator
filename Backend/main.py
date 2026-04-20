import os
import io
from contextlib import asynccontextmanager

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import threading
device = "cuda" if torch.cuda.is_available() else "cpu"
BLIP_PATH = "models/blip"

# Global variables
processor = None
model = None

model_status = {
    "ready": False,
    "loading": True,
    "error": None
}


def is_model_available(path):
    return os.path.exists(path) and len(os.listdir(path)) > 0


def download_blip():
    print("Downloading BLIP model...")

    temp_processor = BlipProcessor.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    temp_model = BlipForConditionalGeneration.from_pretrained(
        "Salesforce/blip-image-captioning-base"
    )

    os.makedirs(BLIP_PATH, exist_ok=True)

    temp_processor.save_pretrained(BLIP_PATH)
    temp_model.save_pretrained(BLIP_PATH)

    print("BLIP model downloaded successfully")


def load_model():
    global processor, model, model_status

    try:
        print("Starting model initialization...")

        if not is_model_available(BLIP_PATH):
            download_blip()

        processor = BlipProcessor.from_pretrained(
            BLIP_PATH,
            local_files_only=True
        )

        model = BlipForConditionalGeneration.from_pretrained(
            BLIP_PATH,
            local_files_only=True
        ).to(device)

        model_status["ready"] = True
        model_status["loading"] = False
        model_status["error"] = None

        print("BLIP model loaded successfully")

    except Exception as e:
        model_status["ready"] = False
        model_status["loading"] = False
        model_status["error"] = str(e)

        print(f"Model loading failed: {e}")


@asynccontextmanager
async def lifespan(app: FastAPI):
    threading.Thread(target=load_model, daemon=True).start()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return model_status


@app.post("/caption")
async def generate_caption(file: UploadFile = File(...)):
    if not model_status["ready"]:
        raise HTTPException(
            status_code=503,
            detail="Model is still loading or failed to load"
        )

    try:
        contents = await file.read()

        image = Image.open(io.BytesIO(contents)).convert("RGB")

        inputs = processor(
            image,
            return_tensors="pt"
        ).to(device)

        output = model.generate(
            **inputs,
            max_new_tokens=30
        )

        caption = processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return {"caption": caption}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Caption generation failed: {str(e)}"
        )


#  LOCAL
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )



## LIVE

# if __name__ == "__main__":
#     import os
#     import uvicorn

#     port = int(os.environ.get("PORT", 8000))

#     uvicorn.run(
#         app,
#         host="0.0.0.0",
#         port=port
#     )