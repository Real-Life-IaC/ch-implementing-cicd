import aws_cdk as cdk

from aws_cdk import aws_s3 as s3
from constructs import Construct


class CiCdStack(cdk.Stack):
    """Simple stack to demo CI/CD"""

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        s3.Bucket(
            scope=self,
            id="Bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            versioned=True,
        )
