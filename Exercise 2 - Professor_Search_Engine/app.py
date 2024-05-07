import streamlit as st
import requests
from bs4 import BeautifulSoup
from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model with trust_remote_code=True
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True)

def scrape_website(url):
    # Send a request to the URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract text from the webpage
    text = ' '.join(p.text for p in soup.find_all('p'))
    return text

def summarize_text(text):
    # Encode the text and generate a summary
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(**inputs, max_length=150, num_return_sequences=1)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Streamlit interface
st.title('Web Scraper and Text Summarizer')
url = st.text_input('Enter the URL of the webpage to scrape and summarize:', '')

if url:
    scraped_text = scrape_website(url)
    summary = summarize_text(scraped_text)
    st.write('Summary:')
    st.write(summary)