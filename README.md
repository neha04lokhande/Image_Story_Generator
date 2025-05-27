# 🖼️ Image Story Generator
 ◦ Developed a web-based application that transforms images into stories by integrating computer vision, NLP.
 ◦ Implemented the BLIP model to generate captions from images Utilized Gemini to craft narratives 
 ◦ Tech Stack: Python, PyTorch, Hugging Face Transformers, Google Generative AI (Gemini), Streamlit




## 🚀 Features

- 📷 Upload any image (JPEG or PNG)
- 🧠 Generate multiple image captions using the BLIP (Bootstrapping Language-Image Pre-training) model
- ✍️ Create a coherent short story based on the captions using Google Gemini AI
- 🎨 Sleek and responsive UI with Streamlit

---

## 📸 Demo

<p align="center">
  <img src="https://imgur.com/your-demo-image.gif" width="80%" alt="demo">
</p>

> Upload an image and watch the magic unfold as AI creates a story from it!

---

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Image Captioning**: [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base)
- **Story Generation**: [Gemini 1.5 Pro API](https://ai.google.dev/)
- **Backend**: Python, Transformers, Torch, PIL

---

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/neha04lokhande/image-story-generator.git
cd image-story-generator


Install Dependencies

Make sure Python 3.7+ is installed. Then install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Set Gemini API Key

Replace the placeholder API key in the code:

python
Copy
Edit
genai.configure(api_key="YOUR_GEMINI_API_KEY")
You can get an API key from Google AI Studio.

Run the App

bash
Copy
Edit
streamlit run app.py

📁 Project Structure
bash
Copy
Edit
.
├── app.py                # Main application script
├── requirements.txt      # List of dependencies
├── README.md             # Project overview and instructions

