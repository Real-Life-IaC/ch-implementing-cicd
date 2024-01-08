import aws_cdk as cdk

from src.stack import MyStack


app = cdk.App()
MyStack(app, "MyStack")
app.synth()
