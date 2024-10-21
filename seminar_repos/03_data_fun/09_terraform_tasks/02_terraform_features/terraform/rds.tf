resource "aws_db_instance" "default" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "14.10"
  instance_class      = "db.t4g.micro"
  username            = var.db_username
  password            = var.db_password
  identifier          = "example-database"
  skip_final_snapshot = true
}
