import streamlit as st
import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import google.generativeai as genai  # Importing Gemini AI API

# Set up Gemini API key (replace with your own Gemini API key)
genai.configure(api_key="###########################")

def load_model():
    """
    Loads the BLIP image captioning model and processor.
    """
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

def generate_captions(image, processor, model, num_captions=5):
    """
    Generates multiple captions for an uploaded image using the BLIP model.
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    image = image.convert('RGB')
    inputs = processor(images=image, return_tensors="pt").to(device)
    
    captions = []
    for _ in range(num_captions):
        output = model.generate(**inputs, max_length=50, num_return_sequences=1, do_sample=True, temperature=0.7)
        caption = processor.decode(output[0], skip_special_tokens=True)
        captions.append(caption)
    
    return captions

def generate_story_from_captions(captions):
    """
    Uses Google Gemini AI to generate a story from the image captions.
    """
    prompt = (
        "Create a short , engaging, and meaningful story in very simple words based on the following image descriptions:\n\n"
        + "\n".join(f"- {caption}" for caption in captions)
        + "\n\nMake it flow naturally like a short story with an introduction, body, and a meaningful ending."
    )

    model = genai.GenerativeModel("gemini-1.5-pro")  # Using Gemini Pro Model
    response = model.generate_content(prompt)

    return response.text  # Extracts and returns the generated story

def main():
    """
    Streamlit UI for uploading an image and generating an AI-written story.
    """
    st.set_page_config(page_title='Image Story Generator', layout='wide', page_icon='📷')
    
    # Custom CSS for better UI
    st.markdown(
        """
        <style>
        .main {background-color: #f0f2f6;}
        .stButton>button {background-color: #4CAF50; color: white; font-size: 16px; padding: 10px; border-radius: 10px;}
        .stFileUploader>label {font-size: 18px; font-weight: bold;}
        .stImage img {border-radius: 15px; max-width: 400px; display: block; margin: auto;}
        .story-box {padding: 15px; background-color: #e8eaf6; border-radius: 15px; font-size: 18px; font-weight: bold; text-align: justify;}
        .stSubheader {color: #333399; font-size: 24px; text-align: center;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title('🖼️ Image Story Generator')
    st.write("### Upload an image and get a unique, AI-generated story!")

    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)

        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)

        with col2:
            with st.spinner('✨ Generating an amazing story... ✨'):
                # Load model
                processor, model = load_model()
                captions = generate_captions(image, processor, model)
                
                # Generate story from captions using Gemini AI
                story = generate_story_from_captions(captions)

                # Display the generated story
                st.subheader("📖 Generated Story:")
                st.markdown(f"<div class='story-box'>{story}</div>", unsafe_allow_html=True)

if __name__ == '__main__':
    main()
