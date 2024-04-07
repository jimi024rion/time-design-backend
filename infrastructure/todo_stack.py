from typing import Any

from aws_cdk import Stack
from constructs import Construct

from infrastructure.api.constract import TodoApi


class TodoAppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs: Any) -> None:
        super().__init__(scope, id, **kwargs)

        TodoApi(self, "TodoApi")
