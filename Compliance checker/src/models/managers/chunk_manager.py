def create_chunks(text, max_chunk_size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks