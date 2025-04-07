def split_text_by_bytes(text, byte_limit=4900):
    """
    Splits text into chunks that stay under the given byte limit.
    Useful for Google Cloud TTS 5000-byte limitation.
    """
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = ""

    for para in paragraphs:
        para_bytes = para.encode("utf-8")
        chunk_bytes = current_chunk.encode("utf-8")

        if len(chunk_bytes) + len(para_bytes) + 2 < byte_limit:
            current_chunk += para + "\n\n"
        else:
            chunks.append(current_chunk.strip())
            current_chunk = para + "\n\n"

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks
