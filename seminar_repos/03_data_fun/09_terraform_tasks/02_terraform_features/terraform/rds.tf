variable "db_username" {
  description = "db_user"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "db_pass"
  type        = string
  sensitive   = true
}


resource "aws_db_instance" "default" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "14.15"
  instance_class      = "db.t4g.micro"
  username            = var.db_username
  password            = var.db_password
  identifier          = "example-db"
  skip_final_snapshot = true
}
