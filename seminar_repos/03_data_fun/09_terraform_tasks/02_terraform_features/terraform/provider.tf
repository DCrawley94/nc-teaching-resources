provider "aws" {
  region = "eu-west-2"
}

terraform {
  backend "s3" {
    bucket = "dc-nc-tf-backend"
    key    = "terraform-features/terraform-features-2.tfstate"
    region = "eu-west-2"
  }
}
