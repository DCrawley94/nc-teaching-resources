resource "aws_db_instance" "default" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "13.18"
  instance_class      = "db.t4g.micro"
  username            = "postgres"
  password            = "password123"
  identifier          = "example-database"
  skip_final_snapshot = true
}
