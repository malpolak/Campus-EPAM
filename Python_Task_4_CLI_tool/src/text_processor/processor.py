from text_processor.decorators import timer
from text_processor.logger import setup_logger
import re

logger = setup_logger()

def clean_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)

    return text

@timer
def process_file(input_path: str, output_path: str):
    logger.info(f"Reading file: {input_path}")

    with open(input_path, "r") as f:
        text = f.read()

    text = clean_text(text)

    words = text.split()

    freq = {}

    for word in words:
        freq[word] = freq.get(word,0) + 1

    result = "\n".join(f"{word}: {count}" for word, count in freq.items())

    with open(output_path, "w") as f:
        f.write(result)

    logger.info("File processed ans written successfully")

