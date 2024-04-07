import aws_cdk as cdk

from infrastructure.todo_stack import TodoAppStack

app = cdk.App()
TodoAppStack(app, "TodoStack")

app.synth()
