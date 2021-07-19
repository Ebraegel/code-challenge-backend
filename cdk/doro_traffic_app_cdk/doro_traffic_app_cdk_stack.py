"""AWS CDK module to create ECS infrastructure"""
from aws_cdk import (core, aws_ecs as ecs, aws_ecr as ecr, aws_ec2 as ec2, aws_iam as iam)

class DoroTrafficAppCdkStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the ECR Repository
        backend_ecr_repository = ecr.Repository(self,
                                        "doro-traffic-backend",
                                        repository_name="doro-traffic-backend")
        ui_ecr_repository = ecr.Repository(self,
                                        "doro-traffic-ui",
                                        repository_name="doro-traffic-ui")

        # Create the ECS Cluster (and VPC)
        vpc = ec2.Vpc(self,
                      "doro-traffic-app-vpc",
                      max_azs=3)
        cluster = ecs.Cluster(self,
                              "doro-traffic-app-cluster",
                              cluster_name="doro-traffic-app-cluster",
                              vpc=vpc)

        # Create the ECS Task Definition with placeholder container (and named Task Execution IAM Role)
        execution_role = iam.Role(self,
                                  "doro-traffic-app-execution-role",
                                  assumed_by=iam.ServicePrincipal("ecs-tasks.amazonaws.com"),
                                  role_name="doro-traffic-app-execution-role")
        execution_role.add_to_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            resources=["*"],
            actions=[
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
                ]
        ))
        task_definition = ecs.FargateTaskDefinition(self,
                                                    "doro-traffic-app-task-definition",
                                                    execution_role=execution_role,
                                                    family="doro-traffic-app-task-definition")
        container = task_definition.add_container(
            "doro-traffic-app",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
        )

        # Create the ECS Service
        service = ecs.FargateService(self,
                                     "doro-traffic-app-service",
                                     cluster=cluster,
                                     task_definition=task_definition,
                                     service_name="doro-traffic-app-service")
