from diagrams import Diagram, Cluster
from diagrams.aws.compute import AutoScaling, EC2
from diagrams.aws.database import Dynamodb
from diagrams.aws.integration import SNS
from diagrams.aws.network import ElasticLoadBalancing
from diagrams.aws.storage import S3
from diagrams.onprem.client import Client, User

with Diagram("Clustered Web Services", show=False):
    client = Client("Client")
    user = User("User")

    with Cluster("AWS Region"):
        with Cluster("Elastic Beanstalk"):
            elb = ElasticLoadBalancing("Elastic Load Balancer")
            with Cluster("Availability Zone A"):
                ec2_zone_a = EC2("Amazon EC2 instance")
            with Cluster("Availability Zone B"):
                ec2_zone_b = EC2("Amazon EC2 Instance")

            s3_bucket = S3("Amazon S3 Bucket")

        dynamoDB = Dynamodb("Amazon Dynamo DB")
        sns = SNS("Amazon SNS")

        user >> client >> elb
        elb >> ec2_zone_a
        elb >> ec2_zone_b

        ec2_zone_a >> s3_bucket
        ec2_zone_b >> s3_bucket

        s3_bucket >> dynamoDB
        s3_bucket >> sns
