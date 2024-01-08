import aws_cdk as cdk

from constructs import Construct


class MyStack(cdk.Stack):
    """Create a Stack with"""

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

