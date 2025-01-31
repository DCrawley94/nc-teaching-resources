provider "aws" {
  region = "eu-west-2"

  default_tags {
    tags = {
      Owner   = "Danika"
      Project = "example"
    }
  }
}



terraform {
  backend "s3" {
    bucket = "dc-nc-tf-backend"
    key    = "terraform-features/terraform-features_2.tfstate"
    region = "eu-west-2"
  }
}

