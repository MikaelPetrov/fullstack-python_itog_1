def safe_filename(text):
    forbidden = '\\/:*?"<>|'
    name = "".join(c for c in text if c not in forbidden).strip()

    return name or "cat"
