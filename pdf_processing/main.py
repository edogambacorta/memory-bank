import sys
import os
from pdf_parser import parse_pdf
from text_preprocessor import preprocess_text
from memory_bank import update_memory_bank

def process_pdf(file_path):
    print(f"Processing {file_path}...")
    
    # Read and parse PDF
    pdf_text = parse_pdf(file_path)
    
    if pdf_text is None:
        print(f"Failed to process {file_path}")
        return

    # Preprocess text
    processed_text = preprocess_text(pdf_text)

    # Update Memory Bank
    update_memory_bank(processed_text)

    print(f"Processed and updated Memory Bank with content from {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <pdf_file1> [pdf_file2 ...]")
        sys.exit(1)

    for pdf_file in sys.argv[1:]:
        if not os.path.exists(pdf_file):
            print(f"File not found: {pdf_file}")
            continue
        if not pdf_file.lower().endswith('.pdf'):
            print(f"Not a PDF file: {pdf_file}")
            continue
        process_pdf(pdf_file)

if __name__ == "__main__":
    main()
