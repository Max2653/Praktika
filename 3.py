import sys
from datetime import datetime

class Logger:
    def __init__(self, out_stream=sys.stderr, time_format='%Y-%m-%d %H:%M:%S'):
        self.out_stream = out_stream
        self.time_format = time_format

    def log(self, message):
        timestamp = datetime.now().strftime(self.time_format)
        print(f"[{timestamp}] {message}", file=self.out_stream)

if __name__ == "__main__":
    logger = Logger()
    logger.log("Test log message")