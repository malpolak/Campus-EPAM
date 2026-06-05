from pathlib import Path
import argparse

from text_processor.processor import process_file
from text_processor.logger import setup_logger

logger = setup_logger()

def resolve_input_path(path: str) -> str:

    p = Path(path)

    # 1. direct path
    if p.exists():
        return str(p)

    # 2. try examples/
    alt = Path("examples") / path
    if alt.exists():
        return str(alt)

    # 3. try src/ project root fallback
    alt2 = Path("src") / path
    if alt2.exists():
        return str(alt2)

    raise FileNotFoundError(f"Input file not found: {path}")

def main():
    parser = argparse.ArgumentParser(description="A CLI tool that processes text files and generates word frequency output.",
                                     epilog="Example: python main.py input.txt output.txt")

    parser.add_argument("input_file", help="Path to input file")
    parser.add_argument("output_file", help="Path to output file")

    args = parser.parse_args()

    try:
        logger.info("Starting processing")

        input_path = resolve_input_path(args.input_file)

        process_file(input_path, args.output_file)

        logger.info("Done")

    except FileNotFoundError as e:
        logger.error(str(e))

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()