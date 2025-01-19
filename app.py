from document_processing.ocr_pipeline import extract_text_from_pdf
from document_processing.preprocess_text import clean_text, detect_sections
from document_processing.knowledge_base import add_to_knowledge_base
from chatbot.chatbot_main import chatbot

def main():
    # Document processing pipeline
    pdf_file = "example.pdf"
    extracted_text = extract_text_from_pdf(pdf_file)
    cleaned_text = clean_text(extracted_text)
    sections = detect_sections(cleaned_text)
    add_to_knowledge_base(sections)
    
    # Chatbot interaction
    while True:
        query = input("Ask a question (type 'exit' to quit): ")
        if query.lower() == 'exit':
            break
        print(chatbot(query))

if __name__ == "__main__":
    main()
