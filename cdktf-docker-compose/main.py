from constructs import Construct
from cdktf import App, TerraformStack, TerraformAsset, AssetType, LocalExecProvisioner
from imports.docker.provider import DockerProvider
from imports.docker.image import Image
from imports.docker.container import Container
from imports.docker.network import Network
from imports.docker.volume import Volume
from imports.null.resource import Resource as NullResource
import os
from imports.null.provider import NullProvider


class MultiContainerStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        DockerProvider(self, "docker", host="unix:///var/run/docker.sock")
        NullProvider(self, "null")  # ✅ Required for null_resource to work



        # Create Docker network
        network = Network(self, "app-network", name="cdktf-net")

        # Redis volume
        redis_volume = Volume(self, "redis-vol", name="redis-data")

        # Redis container
        redis_container = Container(self, "redis",
            name="redis",
            image="redis:7",
            networks_advanced=[{"name": network.name}],
            volumes=[{"containerPath": "/data", "volumeName": redis_volume.name}],
            env=["ALLOW_EMPTY_PASSWORD=yes"],
            ports=[{"internal": 6379, "external": 6379}],
            healthcheck={
                "test": ["CMD", "redis-cli", "ping"],
                "interval": "5s",
                "timeout": "3s",
                "retries": 3
            }
        )

        # Flask app Dockerfile asset
        app_asset = TerraformAsset(self, "app-code",
            path=os.path.abspath("app"),
            type=AssetType.DIRECTORY
        )

        # Build Docker image using null_resource
        docker_build = NullResource(self, "docker-build",
            triggers={"always_run": str(os.urandom(16))},
            provisioners=[
                LocalExecProvisioner(
                    type="local-exec",
                    command=f"docker build -t flask-cdktf {app_asset.path}"
                )
            ]
        )

        # Register the Flask image (already built via null_resource)
        app_image = Image(self, "flask-img",
            name="flask-cdktf",
            keep_locally=True
        )

        # # Flask app container
        # app_container = Container(self, "flask-app",
        #     name="flask-api",
        #     image=app_image.name,
        #     networks_advanced=[{"name": network.name}],
        #     ports=[{"internal": 5000, "external": 5050}],
        #     depends_on=[redis_container, docker_build]  # ✅ Proper object references
        # )

        # # NGINX reverse proxy
        # nginx_container = Container(self, "nginx",
        #     name="nginx-reverse",
        #     image="nginx:latest",
        #     networks_advanced=[{"name": network.name}],
        #     ports=[{"internal": 80, "external": 8080}],
        #     volumes=[{
        #         "containerPath": "/etc/nginx/conf.d",
        #         "hostPath": os.path.abspath("nginx-conf"),
        #         "readOnly": True
        #     }],
        #     depends_on=[app_container]  # ✅ Fixed: object ref only
        # )
        app_container = Container(self, "flask-app",
            name="flask-api",
            image=app_image.name,
            networks_advanced=[{
                "name": network.name
            }],
            # ports=[{
            #     "internal": 5000,
            #     "external": 5050
            # }],
            depends_on=[redis_container, docker_build]  # ✅ Objects, not .fqn
        )

        nginx_container = Container(self, "nginx",
            name="nginx-reverse",
            image="nginx:latest",
            networks_advanced=[{
                "name": network.name
            }],
            ports=[{
                "internal": 80,
                "external": 8080
            }],
            volumes=[{
                "containerPath": "/etc/nginx/conf.d",
                "hostPath": os.path.abspath("nginx-conf"),
                "readOnly": True
            }],
            depends_on=[app_container]  # ✅ object ref, not .fqn
        )


app = App()
MultiContainerStack(app, "docker-multicontainer")
app.synth()
