
resource "aws_instance" "ec2-example" {
  ami             = "ami-091f18e98bc129c4e"
  instance_type   = "t3.micro"
  key_name        = "dc-ssh"
  security_groups = [aws_security_group.allow_ssh.name]
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow SSH inbound traffic"
}

resource "aws_vpc_security_group_ingress_rule" "allow_ssh_ipv4" {
  security_group_id = aws_security_group.allow_ssh.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 22
  ip_protocol       = "tcp"
  to_port           = 22
}
