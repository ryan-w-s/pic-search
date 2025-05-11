from .cli import parse_args
import sys

def main() -> None:
    try:
        args = parse_args()
        print(args)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
