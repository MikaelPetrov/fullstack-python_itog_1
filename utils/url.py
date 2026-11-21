def transform_to_query_str(params: dict):
    if not params:
        return ""

    return "&".join(f"{k}={v}" for k, v in params.items())
