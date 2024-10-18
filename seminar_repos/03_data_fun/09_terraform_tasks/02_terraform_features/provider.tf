terraform {
  backend "s3" {
    bucket = "dc-nc-tf-backend"
    key    = "terraform-seminar-2.tfstate"
    region = "eu-west-2"
  }
}

