"""AWS CDK module to create ECS infrastructure"""
from aws_cdk import (core, aws_ecs as ecs, aws_ecr as ecr, aws_ec2 as ec2, aws_iam as iam, aws_ecs_patterns as ecs_patterns, aws_logs as logs)


class DoroTrafficAppCdkStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create the ECR Repositories
        ecr.Repository(self,
                       "doro-traffic-backend",
                       repository_name="doro-traffic-backend")
        ecr.Repository(self,
                       "doro-traffic-ui",
                       repository_name="doro-traffic-ui")
        ecr.Repository(self,
                       "doro-traffic-nginx",
                       repository_name="doro-traffic-nginx")

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

        logDetail = logs.LogGroup(self, "ecs", log_group_name="ecs", retention=logs.RetentionDays.SIX_MONTHS, removal_policy=core.RemovalPolicy.DESTROY)

        nginx_container = task_definition.add_container(
            "nginx",

            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            logging=ecs.LogDriver.aws_logs(stream_prefix="nginx", log_group=logDetail)

        )
        nginx_container_port_mapping = ecs.PortMapping(container_port=80)
        nginx_container.add_port_mappings(nginx_container_port_mapping)

        ui_container = task_definition.add_container(
            "ui",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            logging=ecs.LogDriver.aws_logs(stream_prefix="ui", log_group=logDetail)
        )
        ui_container_port_mapping = ecs.PortMapping(container_port=3000)
        ui_container.add_port_mappings(ui_container_port_mapping)

        backend_container = task_definition.add_container(
            "backend",
            image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample"),
            logging=ecs.LogDriver.aws_logs(stream_prefix="backend", log_group=logDetail)
        )
        backend_container_port_mapping = ecs.PortMapping(container_port=5000)
        backend_container.add_port_mappings(backend_container_port_mapping)

        service = ecs_patterns.ApplicationLoadBalancedFargateService(self,
                                                           "doro-traffic-app-service",
                                                           cluster=cluster,
                                                           task_definition=task_definition,
                                                           service_name="doro-traffic-app-service",
                                                           )
