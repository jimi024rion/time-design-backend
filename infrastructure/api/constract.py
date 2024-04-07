from typing import Any

from aws_cdk import aws_apigatewayv2 as apigwv2
from aws_cdk import aws_apigatewayv2_integrations as apigwv2_integrations
from aws_cdk import aws_lambda as _lambda
from aws_cdk import aws_lambda_python_alpha as lambda_alpha
from constructs import Construct


class TodoApi(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs: Any) -> None:
        super().__init__(scope, id, **kwargs)

        # Lambda
        self.todos_fn = lambda_alpha.PythonFunction(
            self,
            "TodoItemHandler",
            entry="src/todo_api",
            index="app.py",
            handler="lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_12,
            # TODO: 環境変数追加(powertool, LogLevelなど)
            # environment={
            #     "LOG_LEVEL": "INFO",
            # },
        )

        # CloudWatchLogs for Lambda
        self.todos_fn.log_group

        # API Gateway
        todos_integrations = apigwv2_integrations.HttpLambdaIntegration(
            "TodoApiIntegration",
            handler=self.todos_fn,
        )
        self.todo_api_gateway = apigwv2.HttpApi(
            self,
            "TodoApiGateway",
            default_integration=todos_integrations,
        )
