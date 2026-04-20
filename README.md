# 🖼️ Image Caption Generator using BLIP (CLI)

A lightweight **command-line image captioning project** that generates natural language descriptions from images using the pretrained **BLIP (Bootstrapping Language-Image Pretraining)** model from Hugging Face.

This project runs **fully locally after first download** and uses **PyTorch + Transformers** for inference.

---

# 🚀 Project Objective

The goal of this project is to take an input image and automatically generate a meaningful textual caption describing the major objects and scene present in it.

### Example

**Input Image:** dog on grass  
**Output Caption:**  
`a dog running in a grassy field`

This is a classic **Computer Vision + NLP multimodal task**.

---

# 🧠 Model Used

This project uses: 
**BLIP – `Salesforce/blip-image-captioning-base`**

Model link:  
https://huggingface.co/Salesforce/blip-image-captioning-base

---

# 🔥 What is BLIP?

BLIP stands for:

**Bootstrapping Language-Image Pretraining**

It is a state-of-the-art **vision-language model** designed for tasks like:

- image captioning
- visual question answering
- image-text retrieval
- multimodal understanding

Unlike older captioning models, BLIP jointly learns:

- how to understand images
- how to generate text

This makes captions more natural and context-aware.

---

# ⚙️ How BLIP Works (Simple Flow)

```text
Input Image
   ↓
Image Preprocessing
   ↓
Vision Transformer Encoder
   ↓
Feature Embeddings
   ↓
Text Decoder
   ↓
Generated Caption
```

---

## 👁️ Step 1: Image Encoder
The image is first resized and normalized.

Then it is split into small patches.

Example:

```text
224 × 224 image
→ 16 × 16 patches
```

These patches are converted into embeddings using a **Vision Transformer (ViT)**.

This helps the model understand:

- objects
- colors
- positions
- scene context

---

## 📝 Step 2: Text Decoder
The visual embeddings are passed to the text generation decoder.

The decoder predicts words **token by token**.

Example:

```text
a
dog
running
in
grass
```

This is autoregressive text generation.

---

# 💡 Why BLIP is Powerful

BLIP was trained on large-scale image-text data from the internet.

A major innovation is **bootstrapping**, where the model improves noisy captions by generating better synthetic text during training.

This helps improve caption quality significantly.

---

# 📁 Project Structure

```text
company/
│── app.py
│── requirements.txt
│── models/
│    └── blip/
│── assets/
│── .gitignore
│── README.md
```

---

# ⚙️ Installation

Follow these steps to set up the project locally.

---

## 1. Clone Repository

```bash
git clone https://github.com/BipulRahi/image-caption-generator.git
cd image-caption-generator
```

---

## 2. Create Virtual Environment

### Windows
```bash
python -m venv cleanenv
cleanenv\Scripts\activate
```

### Linux / macOS
```bash
python3 -m venv cleanenv
source cleanenv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Verify Installation

```bash
pip list
```

Expected important packages:

- torch
- transformers
- pillow
- torchvision
- numpy

---

# 🚀 How to Run

Run the CLI application:

```bash
python app.py
```

---

# 🖼 Example Run

```text
Enter image path: ./assets/dog.jpg
🔍 Checking model availability...
✅ Model found locally
🧠 Generating caption...
------------------------------------------------------------
a dog running in a grassy field
------------------------------------------------------------
```

---

# 💾 First-Time Model Download

If the BLIP model is not available locally, the script automatically asks:

```text
⚠️ Model not found. Download now? (y/n):
```

Press:

```text
y
```

The model will be downloaded once and saved inside:

```text
models/blip/
```

After that, future runs use the local model directly.

---

# 📂 Supported Image Formats

The script supports:

- `.jpg`
- `.jpeg`
- `.png`

Example:

```text
./asserts/sample.jpg
```

---

# 🔁 Multiple Image Testing

The latest code supports repeated image caption generation in the same run.

Example:

```text
Enter image path: ./asserts/dog.jpg
Enter image path: ./asserts/cat.jpg
Enter image path: exit
```

---

# 🛠 Common Errors

---

## ❌ Invalid image path

```text
❌ Invalid image path
```

Fix:
Ensure the file exists.

Correct:

```text
./asserts/dog.jpg
```

Wrong:

```text
./assets
```

---

## ❌ Model download cancelled

```text
❌ Exiting. No model loaded.
```

Run again and choose:

```text
y
```

---

# 🧠 Tech Stack

- Python
- TORCH
- Transformers
- PIL
- Vision Transformer
- BLIP

---


# 📚 References

BLIP model:  
https://huggingface.co/Salesforce/blip-image-captioning-base

BLIP paper:  
https://arxiv.org/abs/2201.12086
