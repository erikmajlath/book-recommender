# logs.tf

# Set up CloudWatch group and log stream and retain logs for 30 days
resource "aws_cloudwatch_log_group" "br_log_group" {
  name              = "/ecs/br-app"
  retention_in_days = 30

  tags = {
    Name = "br-log-group"
  }
}

resource "aws_cloudwatch_log_stream" "br_log_stream" {
  name           = "br-log-stream"
  log_group_name = aws_cloudwatch_log_group.br_log_group.name
}

