from PyPDF2 import PdfReader

def validate_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        if len(reader.pages) == 0:
            return False
        return True
    except Exception as e:
        print(f"PDF validation error: {e}")
        return False
