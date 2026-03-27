from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput
from imports.aws.provider import AwsProvider
from imports.aws.vpc import Vpc
from imports.aws.subnet import Subnet
from imports.aws.internet_gateway import InternetGateway
from imports.aws.route_table import RouteTable, RouteTableRoute
from imports.aws.route_table_association import RouteTableAssociation
from imports.aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
from imports.aws.instance import Instance
from imports.aws.key_pair import KeyPair
import os


class MyVMStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # 🔧 Set common tags
        common_tags = {
            "Environment": "Dev",
            "Owner": "YourName",
            "Project": "CDKTF-Lab"
        }

        # ✅ AWS Provider
        AwsProvider(self, "AWS", region="ap-south-1")

        # ✅ VPC
        vpc = Vpc(self, "MainVPC",
            cidr_block="10.0.0.0/16",
            tags={**common_tags, "Name": "MainVPC"}
        )

        # ✅ Subnet
        subnet = Subnet(self, "PublicSubnet",
            vpc_id=vpc.id,
            cidr_block="10.0.1.0/24",
            availability_zone="ap-south-1a",
            tags={**common_tags, "Name": "PublicSubnet"}
        )

        # 🌐 Internet Gateway
        igw = InternetGateway(self, "InternetGateway",
            vpc_id=vpc.id,
            tags={**common_tags, "Name": "CDKTF-IGW"}
        )

        # 🛣️ Route Table
        route_table = RouteTable(self, "PublicRouteTable",
            vpc_id=vpc.id,
            route=[RouteTableRoute(
                cidr_block="0.0.0.0/0",
                gateway_id=igw.id
            )],
            tags={**common_tags, "Name": "PublicRouteTable"}
        )

        # 🔗 Route Table Association
        RouteTableAssociation(self, "PublicSubnetAssociation",
            subnet_id=subnet.id,
            route_table_id=route_table.id
        )

        # ✅ Security Group
        sg = SecurityGroup(self, "InstanceSG",
            name="allow-ssh",
            vpc_id=vpc.id,
            ingress=[SecurityGroupIngress(
                from_port=22,
                to_port=22,
                protocol="tcp",
                cidr_blocks=["0.0.0.0/0"]
            )],
            egress=[SecurityGroupEgress(
                from_port=0,
                to_port=0,
                protocol="-1",
                cidr_blocks=["0.0.0.0/0"]
            )],
            tags={**common_tags, "Name": "InstanceSG"}
        )

        # 🔐 Automatically read public key from ~/.ssh/cdktf-key.pub
        public_key_path = os.path.expanduser("~/.ssh/cdktf-key.pub")

        with open(public_key_path, "r") as pk_file:
            ssh_public_key = pk_file.read().strip()

        # 🔐 SSH Key Pair
        key_pair = KeyPair(self, "MyKey",
            key_name="cdktf-key",
            public_key=ssh_public_key,
            tags={**common_tags, "Name": "cdktf-key"}
        )

        # 📦 user_data to install Docker
        # 📂 Load user_data script from file
        user_data_path = os.path.abspath("setup-docker.sh")
        with open(user_data_path, "r") as f:
            user_data_script = f.read()


        # ✅ EC2 Instance
        ec2_instance = Instance(self, "MyInstance",
            ami="ami-0f918f7e67a3323f0",  # Make sure it's valid in ap-south-1
            instance_type="t2.micro",
            subnet_id=subnet.id,
            associate_public_ip_address=True,
            vpc_security_group_ids=[sg.id],
            key_name=key_pair.key_name,
            user_data=user_data_script,
            tags={**common_tags, "Name": "CDKTF-VM"}
        )

        # ✅ Output Public IP & SSH command
        TerraformOutput(self, "public_ip",
            value=ec2_instance.public_ip
        )

        TerraformOutput(self, "ssh_hint",
            value=f"ssh -i ~/.ssh/cdktf-key ubuntu@{ec2_instance.public_ip}"
        )


app = App()
MyVMStack(app, "vm-stack")
app.synth()


















# from constructs import Construct
# from cdktf import App, TerraformStack, TerraformOutput
# from imports.aws.provider import AwsProvider
# from imports.aws.vpc import Vpc
# from imports.aws.subnet import Subnet
# from imports.aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
# from imports.aws.instance import Instance



# class MyVMStack(TerraformStack):
#     def __init__(self, scope: Construct, id: str):
#         super().__init__(scope, id)

#         # ✅ AWS Provider
#         AwsProvider(self, "AWS", region="ap-south-1")

#         # ✅ VPC
#         vpc = Vpc(self, "MainVPC",
#             cidr_block="10.0.0.0/16"
#         )

#         # ✅ Subnet
#         subnet = Subnet(self, "PublicSubnet",
#             vpc_id=vpc.id,
#             cidr_block="10.0.1.0/24",
#             availability_zone="ap-south-1a"
#         )

#         # ✅ Security Group (Correct typed way)
#         sg = SecurityGroup(self, "InstanceSG",
#             name="allow-ssh",
#             vpc_id=vpc.id,
#             ingress=[SecurityGroupIngress(
#                 from_port=22,
#                 to_port=22,
#                 protocol="tcp",
#                 cidr_blocks=["0.0.0.0/0"]
#             )],
#             egress=[SecurityGroupEgress(
#                 from_port=0,
#                 to_port=0,
#                 protocol="-1",
#                 cidr_blocks=["0.0.0.0/0"]
#             )]
#         )


#         # ✅ EC2 Instance
#         ec2_instance = Instance(self, "MyInstance",
#             ami="ami-0f918f7e67a3323f0",  # Ubuntu 22.04 LTS (us-east-1)
#             instance_type="t2.micro",
#             subnet_id=subnet.id,
#             vpc_security_group_ids=[sg.id],
#             tags={"Name": "CDKTF-VM"}
#         )

#         # ✅ Output Public IP (optional but helpful)
#         TerraformOutput(self, "public_ip",
#             value=ec2_instance.public_ip
#         )

# app = App()
# MyVMStack(app, "vm-stack")
# app.synth()
