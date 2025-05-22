def extract_auth(config: dict) -> tuple[str, str]:
    """Safely extract client_id and token from LangGraph config."""
    try:
        auth = config.get("configurable", {}).get("auth", {})
        return auth["client_id"], auth["user_token"]
    except KeyError as e:
        raise ValueError(f"Missing authentication key in config: {e}")
