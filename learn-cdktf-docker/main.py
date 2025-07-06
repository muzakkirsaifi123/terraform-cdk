from constructs import Construct
from cdktf import App, TerraformStack
from imports.docker.provider import DockerProvider
from imports.docker.image import Image
from imports.docker.container import Container


class MyDockerStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)

        # Initialize Docker provider
        DockerProvider(self, "docker", host="unix:///var/run/docker.sock")

        # Pull nginx image
        image = Image(self, "nginx-image",
                      name="nginx:latest",
                      keep_locally=False)

        # Create container
        Container(self, "nginx-container",
                  image=image.name,
                  name="nginx-cdktf",
                  ports=[{
                      "internal": 80,
                      "external": 8080,
                  }])

app = App()
MyDockerStack(app, "docker-demo")
app.synth()
