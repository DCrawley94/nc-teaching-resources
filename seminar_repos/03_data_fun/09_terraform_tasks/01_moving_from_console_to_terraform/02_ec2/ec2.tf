resource "aws_instance" "example-ec2" {
  ami             = "ami-0acc77abdfc7ed5a6"
  instance_type   = "t2.micro"
  key_name        = "dc-ssh"
  security_groups = [aws_security_group.ec2-example-sg.name]
}

resource "aws_security_group" "ec2-example-sg" {
  name        = "example"
  description = "allow ssh access into the instance"
}

resource "aws_vpc_security_group_ingress_rule" "ec2-ssh" {
  security_group_id = aws_security_group.ec2-example-sg.id

  cidr_ipv4   = "0.0.0.0/0"
  from_port   = 22
  to_port     = 22
  ip_protocol = "tcp"
}
