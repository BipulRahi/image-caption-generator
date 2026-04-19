import os
from PIL import Image
import torch

from transformers import (
    BlipProcessor, BlipForConditionalGeneration
)
# CONFIG
device = "cuda" if torch.cuda.is_available() else "cpu"

BLIP_PATH = "models/blip"

# Helper Functions
def is_model_available(path):
    return os.path.exists(path) and len(os.listdir(path)) > 0


def download_blip():
    print("⬇️ Downloading BLIP model...")
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    os.makedirs(BLIP_PATH, exist_ok=True)
    processor.save_pretrained(BLIP_PATH)
    model.save_pretrained(BLIP_PATH)

    print("✅ BLIP model downloaded successfully")

def load_blip():
    print("🚀 Loading BLIP model...")
    processor = BlipProcessor.from_pretrained(BLIP_PATH, local_files_only=True)
    model = BlipForConditionalGeneration.from_pretrained(
        BLIP_PATH, local_files_only=True
    ).to(device)
    return processor, model


def ensure_model():
    print("🔍 Checking model availability...")
    if is_model_available(BLIP_PATH):
        print("✅ Model found locally")
        return

    choice = input("⚠️ Model not found. Download now? (y/n): ").strip().lower()

    if choice != "y":
        print("❌ Exiting. No model loaded.")
        exit()

    download_blip()


def generate_caption(image_path):
    if not os.path.exists(image_path):
        print("❌ Invalid image path")
        return

    image = Image.open(image_path).convert("RGB")

    print("🧠 Generating caption...")

    processor, model = load_blip()
    inputs = processor(image, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=30)
    caption = processor.decode(output[0], skip_special_tokens=True)

    print("-"*60)
    print(f"\033[1;30;43m  {caption}  \033[0m")

# MAIN
def main():
    image_path = input("Enter image path: ").strip()
    ensure_model()
    generate_caption(image_path)


if __name__ == "__main__":
    main()
