import time
from datetime import datetime

while True:
    print(f"[{datetime.now()}] Hello from a non-web Python app running in Kubernetes")
    time.sleep(5)
