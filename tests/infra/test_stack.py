import pytest

from aws_cdk.assertions import Template


@pytest.mark.parametrize(
    argnames=["type", "count"],
    argvalues=[
        ("AWS::S3::Bucket", 1),
    ],
)
def test_resource_count(type, count, template: Template):
    template.resource_count_is(type=type, count=count)


def test_bucket(template: Template):
    template.has_resource_properties(
        type="AWS::S3::Bucket",
        props={
            "PublicAccessBlockConfiguration": {
                "BlockPublicAcls": True,
                "BlockPublicPolicy": True,
                "IgnorePublicAcls": True,
                "RestrictPublicBuckets": True,
            },
            "VersioningConfiguration": {"Status": "Enabled"},
            "BucketEncryption": {
                "ServerSideEncryptionConfiguration": [
                    {
                        "ServerSideEncryptionByDefault": {
                            "SSEAlgorithm": "AES256"
                        }
                    }
                ]
            },
        },
    )
