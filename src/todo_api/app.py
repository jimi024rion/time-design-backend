from typing import Any, Dict


def lambda_handler(event: Dict[str, Any], context: object) -> Dict[str, Any]:
    """Sample func"""
    return {"message": "Hello World"}
