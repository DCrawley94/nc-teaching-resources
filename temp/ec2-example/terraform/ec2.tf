resource "aws_instance" "new_ec2" {
  ami             = "ami-026b2ae0ba2773e0a"
  instance_type   = "t2.micro"
  key_name        = "dc-ssh"
  security_groups = [aws_security_group.ec2-ssh.name]

  tags = {
    Name        = "terraform-tasks"
    Environment = "seminar-example"
  }
}

resource "aws_security_group" "ec2-ssh" {
  name        = "terraform-group"
  description = "Allow ssh traffic to terraform created ec2"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name        = "terraform-tasks"
    Environment = "seminar-example"
  }
}
