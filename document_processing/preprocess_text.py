import re
import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(raw_text):
    cleaned_text = re.sub(r'\n{2,}', '\n', raw_text)
    cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
    return cleaned_text

def detect_sections(cleaned_text):
    doc = nlp(cleaned_text)
    sections = {}
    current_section = "Introduction"
    sections[current_section] = []

    for sent in doc.sents:
        if sent.text.strip().endswith(":"):
            current_section = sent.text.strip()
            sections[current_section] = []
        else:
            sections[current_section].append(sent.text.strip())
    return sections
