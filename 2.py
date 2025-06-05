import sys
from datetime import datetime

def log(message):
    #[����-��-�� ��:��:��]
    timestamp = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    #[2025-05-26 12:45:56]
    print(f"{timestamp} {message}", file=sys.stderr)


if __name__ == "__main__":
    log("Test log message")