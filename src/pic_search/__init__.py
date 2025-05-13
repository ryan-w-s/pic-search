from .cli import parse_args
import sys
import logging

def main() -> None:
    try:
        args = parse_args()
        logging.debug(f"Arguments: {args}")
    except ValueError as e:
        logging.error(str(e))
        sys.exit(1)
