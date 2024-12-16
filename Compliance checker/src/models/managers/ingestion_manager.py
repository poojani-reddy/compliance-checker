from PyPDF2 import PdfReader


def extract_text(file_path):
    try:
        reader = PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages])
        return text
    except Exception as e:
        raise Exception(f"Error extracting text: {e}")
