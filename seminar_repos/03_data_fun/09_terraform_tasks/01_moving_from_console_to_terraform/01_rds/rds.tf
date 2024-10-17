resource "aws_db_instance" "rds_example" {
  allocated_storage   = 10
  engine              = "postgresql"
  engine_version      = "14.10"
  instance_class      = "db.t3.micro"
  username            = "postgres"
  password            = "password123"
  identifier          = "rds-example"
  skip_final_snapshot = true
}
