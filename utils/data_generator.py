import uuid

def random_username(prefix="user"):
    return f"{prefix}_{uuid.uuid4().hex[:8]}"
