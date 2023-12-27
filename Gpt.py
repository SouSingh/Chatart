import os
import fitz  # PyMuPDF library for PDF handling

def file_fetcher():
    folder_path = "./data"
    data_array = []

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if it's a file
            if os.path.isfile(file_path):
                try:
                    # Check if it's a PDF file
                    if file_path.lower().endswith(".pdf"):
                        with fitz.open(file_path) as pdf_document:
                            # Extract text from each page
                            text = ""
                            for page_number in range(pdf_document.page_count):
                                page = pdf_document[page_number]
                                # Use pdfminer to extract text with specified encoding
                                text += page.get_text('text', clip=None, level=0, fontsize=0, fontname='id', flags=0, colorspace='', rect=None, text_colorspace='', text_alpha=0, text_flags=0, text_encoding='utf-8', scale=0)
                            data_array.append(text)
                    else:
                        # For non-PDF files, assume they are plain text
                        with open(file_path, 'r', encoding='utf-8') as file:
                            file_content = file.read()
                            data_array.append(file_content)
                except Exception as e:
                    print(f"Error reading file {filename}: {e}")

    return data_array

# Now you can pass the data_array to your language model
