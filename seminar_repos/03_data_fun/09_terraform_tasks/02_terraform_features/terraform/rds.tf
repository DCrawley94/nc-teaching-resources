resource "aws_db_instance" "default" {
  allocated_storage   = 20
  engine              = "postgres"
  engine_version      = "14.15"
  instance_class      = "db.t4g.micro"
  username            = "postgres"
  password            = "password123"
  identifier          = "example-db"
  skip_final_snapshot = true
}
