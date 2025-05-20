import random

def check_liveness(image_path: str) -> bool:
    # TODO: Implement real liveness detection
    # For now, simulate a pass with 90% success
    return random.random() > 0.1
