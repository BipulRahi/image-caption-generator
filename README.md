# 🖼️ Image Caption Generator using BLIP and ViT-GPT2

This project generates **natural language captions from images** using state-of-the-art pretrained vision-language models from Hugging Face.

It supports two models:

- **BLIP** — Salesforce
- **ViT-GPT2** — NLP Connect

The project works in **Command Line Interface (CLI)** mode and can also be extended to UI deployment.

---

# 🚀 Project Objective

The goal of this project is to take an input image and automatically generate a textual description of the major objects and scene present in it.

Example:

Input Image → Dog sitting on beach  
Output →  
`a dog sitting on the beach near the sea`

This is a classic **Image Captioning** problem in Computer Vision + NLP.

---

# 🧠 Models Used

---

## 1) BLIP (Bootstrapping Language-Image Pretraining)

Model Link:  
https://huggingface.co/Salesforce/blip-image-captioning-base

Paper:  
BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation :contentReference[oaicite:0]{index=0}

---

## 🔥 What is BLIP?

BLIP is one of the most advanced image captioning models.

It is designed for both:

- understanding images
- generating language

Unlike older captioning systems that only focus on caption generation, BLIP is a **unified vision-language framework**. :contentReference[oaicite:1]{index=1}

---

## 🧠 Simple intuition

Think of BLIP as two brains working together:

### 👁️ Vision Brain
Understands image content

Example:
- dog
- beach
- sky
- human

This is done using a **Vision Transformer (ViT)** backbone. :contentReference[oaicite:2]{index=2}

---

### 📝 Language Brain
Converts visual understanding into human-readable sentence

Example:
`a dog sitting on the beach`

This is done using a transformer-based text decoder. :contentReference[oaicite:3]{index=3}

---

## ⚙️ How BLIP Works Internally

---

### Step 1: Image Preprocessing
Input image is resized and normalized.

Example:
224 × 224 RGB

---

### Step 2: Patch Creation
The image is divided into small patches.

Example:
16 × 16 patches

Exactly like words in NLP.

---

### Step 3: Vision Transformer
Each patch is converted into embeddings.

This helps the model understand:

- objects
- shapes
- positions
- context

---

### Step 4: Cross-modal Fusion
Image features are passed to text decoder.

This is where image + language understanding happens.

---

### Step 5: Text Generation
Sentence is generated token by token.

Example:

`a`  
`dog`  
`sitting`  
`on`  
`the`  
`beach`

---

## 💡 Why BLIP is powerful

The major contribution from the paper is:

### **Bootstrapping**
BLIP generates synthetic captions and filters noisy image-text pairs from web-scale data. :contentReference[oaicite:4]{index=4}

This improves training quality significantly.

In simple words:

> Model learns from internet images + cleans noisy captions itself

This was a major paper contribution.

---

---

# 2) ViT-GPT2 Image Captioning

Model Link:  
https://huggingface.co/nlpconnect/vit-gpt2-image-captioning

:contentReference[oaicite:5]{index=5}

---

## 🧠 Intuition

This model combines two famous architectures:

- **ViT** = Vision Transformer
- **GPT-2** = Text Generator

This is a classic **Encoder-Decoder Architecture**. :contentReference[oaicite:6]{index=6}

---

## 👁️ Encoder = ViT

ViT converts image into feature vectors.

Image → patches → embeddings

Same as BLIP encoder idea.

---

## 📝 Decoder = GPT-2

GPT-2 generates text from image embeddings.

Example:

`a cat sleeping on sofa`

This is auto-regressive generation.

Meaning:

Each next word depends on previous word.

---

## ⚙️ Architecture Flow

Image  
↓  
ViT Encoder  
↓  
Visual Embeddings  
↓  
GPT-2 Decoder  
↓  
Caption Text

:contentReference[oaicite:7]{index=7}

---

## 💡 Why use this?

This is simple and very effective.

Best for learning:

- encoder-decoder architecture
- multimodal AI
- image-to-text generation

---

# 📁 Project Structure

```text
company/
│── app.py          # Streamlit UI version
│── appp.py         # CLI version
│── requirements.txt
│── models/
│    ├── blip/
│    └── vit_gpt2/
│── assets/
│── .gitignore



# ⚙️ Installation

Follow the steps below to set up and run the project locally.

---

## 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/image-caption-generator.git
cd image-caption-generator
```

---

## 2. Create a Virtual Environment

It is recommended to use a virtual environment to avoid dependency conflicts.

### Windows
```bash
python -m venv cleanenv
cleanenv\Scripts\activate
```

### macOS / Linux
```bash
python3 -m venv cleanenv
source cleanenv/bin/activate
```

---

## 3. Install Dependencies

Install all required packages from `requirements.txt`.

```bash
pip install -r requirements.txt
```

---

## 4. Verify Installation

You can verify the installed packages by running:

```bash
pip list
```

Expected major packages:

- torch
- torchvision
- transformers
- pillow
- numpy

---

# 🚀 How to Use

This project supports **two modes**:

1. **Interactive Mode**
2. **Direct Command Mode**

---

## 🟢 Interactive Mode

Run the script without any command-line arguments.

```bash
python appp.py
```

The application will ask:

- which model to use
- image path
- whether model needs to be downloaded

Example:

```text
🧠 Image Caption Generator

Choose model:
1. BLIP (Salesforce)
2. ViT-GPT2 (nlpconnect)

Enter choice: 1
Enter image path: ./assets/sample.jpg
```

Output:

```text
🧠 Generating caption...

Caption:
a woman sitting on the beach with her dog
```

---

## 🔵 Direct Command Mode

You can directly provide the model and image path.

### Using BLIP

```bash
python appp.py --model blip --image ./assets/sample.jpg
```

---

### Using ViT-GPT2

```bash
python appp.py --model vit --image ./assets/sample.jpg
```

---

## 🧠 Supported Models

### BLIP
```bash
--model blip
```

Uses:
Salesforce/blip-image-captioning-base

---

### ViT-GPT2
```bash
--model vit
```

Uses:
nlpconnect/vit-gpt2-image-captioning

---

# 📂 Input Image Format

Supported formats:

- `.jpg`
- `.jpeg`
- `.png`

Example:

```bash
./assets/dog.jpg
```

---

# 💾 Model Download Behavior

The first time the selected model is used:

- the model is downloaded automatically
- stored inside the `models/` folder
- reused for future runs

This avoids repeated downloads.

---

# 🛠 Example Workflow

```bash
python appp.py --model blip --image ./assets/test.jpg
```

Expected flow:

```text
Checking model availability...
Model found locally
Loading model...
Generating caption...

Caption:
a dog running in a grassy field
```

---

# ❌ Common Errors

### Invalid image path

```text
Invalid image path
```

Fix:
Ensure the image file exists.

Correct example:

```bash
python appp.py --model blip --image ./assets/cat.jpg
```

---

### Model not found

The script will automatically ask:

```text
Model not found locally.
Download now? (y/n)
```

Choose `y`.

---

# 🔁 Re-running the Project

Every time you want to run again:

```bash
cleanenv\Scripts\activate
python appp.py
```

On Linux/macOS:

```bash
source cleanenv/bin/activate
python appp.py
```
