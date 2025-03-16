import sys
import logging

logging.basicConfig(
    filename='app_log.txt',  # Specify the file where logs will be saved
    level=logging.INFO,  # Set the log level, you can change it to DEBUG, WARNING, ERROR, etc.
    format='%(asctime)s - %(message)s',  # Format for the log output (date, time, and message)
    datefmt='%Y-%m-%d %H:%M:%S'  # Date and time format (no milliseconds)
)


command = sys.stdin.readline().strip().upper()
message = sys.stdin.readline().strip()
logging.info(f"[{command}] {message}")
sys.stdout.flush()