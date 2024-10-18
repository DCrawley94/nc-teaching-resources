# Seminar 2

Useful links:

[Terraform Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

## Learning Objectives

- Know how to manage remote state in Terraform
- Know some useful tools to avoid repetition in Terraform code
- Know how to handle sensitive information in Terraform
- Understand the benefits of tagging in AWS and Terraform

**"Theme" of the seminar - I'm now working in a start up and can't just rely on local Terraform state. What do?**

## Starter Task: Refactor yesterdays seminar examples to use remote state

**Danika's ~~Decorators~~ Cloud Engineers!**

- Premise is that I'm expanding my business, gonna have more people working with on my aws infrastructure and as such I can't just work with a local state file anymore!

Tell students that I've decided that the work I was doing with terraform yesterday is now going to be a team project. Local state is now no longer enough, I need to use remote state.

Have studes walk me through the steps I need to take to set up remote terraform state.

- s3 bucket > can I do this with terraform? Get students to walk me through it

- How do I tell Terraform to use the remote bucket?

```hcl
terraform {
  backend "s3" {
    bucket = "dc-nc-tf-backend"
    key    = "terraform-seminar-2.tfstate"
    region = "eu-west-2"
  }
}
```

## Next Step - I Need To Give Others Access To Use Terraform With My Backend

Pick someone to be my first new member of staff.

What do we need for this?

- credentials of some kind

Can show in the browser how we might create a user. As we might want to create a range of resources I'm gonna give blanket admin permissions.

Now let's recreate that in Terraform

```hcl
resource "aws_iam_user" "colleague_1" {
  name = "geoff"
}


data "aws_iam_policy_document" "tf-state-access" {
  statement {
    effect    = "Allow"
    actions   = ["*"]
    resources = ["*"]
  }
}

resource "aws_iam_user_policy" "tf-state-access" {
  name   = "tf-state-access"
  user   = aws_iam_user.colleague_1.name
  policy = data.aws_iam_policy_document.tf-state-access.json
}
```

Can show this working by exporting `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`. Explain that Terraform will prioritise environment variables over my aws config file.

Prove this by running `aws sts get-caller-identity` and then adding/removing a new s3 bucket

```hcl
resource "aws_s3_bucket" "test-bucket-2" {
  bucket_prefix = "test-bucket-2-"
}
```

## Now it's time for more staff

Pick some more people to be my new staff members and start coding more iam users:

```hcl
resource "aws_iam_user" "colleague_2" {
  name = "mildred"
}

resource "aws_iam_user_policy" "tf-state-access-2" {
  name   = "tf-state-access-2"
  user   = aws_iam_user.colleague_2.name
  policy = data.aws_iam_policy_document.tf-state-access.json
}
```

```hcl
resource "aws_iam_user" "colleague_3" {
  name = "reginald"
}

resource "aws_iam_user_policy" "tf-state-access-3" {
  name   = "tf-state-access-2"
  user   = aws_iam_user.colleague_3.name
  policy = data.aws_iam_policy_document.tf-state-access.json
}
```

Ask students if they can see any issues with the way that I'm approaching the problem - **NOT DRY** 😱

## Refactor to use loops

**Bare in mind that terraform apply will complain due to keys being added in the console - THIS IS A GOOD OPPORTUNITY TO SAY WHY FUCKING AROUND IN THE CONSOLE IS BAD**

Link: https://developer.hashicorp.com/terraform/language

**Under resources/meta-arguments**

count: https://developer.hashicorp.com/terraform/language/meta-arguments/count

First attempt:

```hcl
resource "aws_iam_user" "colleagues" {
  count = length(["colleague_1", "colleague_2", "colleague_3"])
  name  = "${["colleague_1", "colleague_2", "colleague_3"][count.index]}_tf_admin_access"
}
```

_Awful. Terrible. Not dry. Take a lap._

```hcl
variable "colleagues" {
  type    = list(string)
  default = ["colleague_1", "colleague_2", "colleague_3"]
}

resource "aws_iam_user" "colleagues" {
  count = length(var.colleagues)
  name  = "${var.colleagues[count.index]}_tf_admin_access"
}

resource "aws_iam_user_policy" "colleague-tf-admin-access" {
  count  = length(var.colleagues)
  name   = "${var.colleagues[count.index]}_tf_admin_access"
  user   = aws_iam_user.colleagues[count.index].name
  policy = data.aws_iam_policy_document.tf-admin-access.json
}
```

_Much better ✨_

### An alternative - `foreach`

```hcl
variable "colleagues" {
  type    = list(string)
  default = ["colleague_1", "colleague_2", "colleague_3"]
}

resource "aws_iam_user" "colleagues" {
  for_each = toset(var.colleagues)

  name = "${each.key}_tf_admin_access"
}

resource "aws_iam_user_policy" "colleague-tf-admin-access" {
  for_each = aws_iam_user.colleagues

  name   = "${each.key}_tf_admin_access"
  user   = each.value.name
  policy = data.aws_iam_policy_document.tf-admin-access.json
}
```

_Lovely jubbly_

## Handling sensitive info

vars:

```hcl
variable "db_username" {
  description = "Database administrator username"
  type        = string
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
}
```

rds:

```hcl
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
```

Show what happens when I run terraform plan with just vars

Have to type it in and it will show in output/state.

Next mark as `sensitive`:

```hcl
variable "db_username" {
  description = "Database administrator username"
  type        = string
  sensitive   = true
}

variable "db_password" {
  description = "Database administrator password"
  type        = string
  sensitive   = true
}
```

Run `terraform plan` and see the difference.

**It's a big ol' pain entering this stuff manually - what do?**

`.tfvars` to the rescue!

```hcl
<!-- .tfvars files -->

db_username = "postgres"
db_password = "password123"
```

And to use this file we run `terraform plan -var-file='.tfvars'`

And of course we should put this file in the `.gitignore`!

---

This isn't the only way to handle sensitive info but it is a good way of doing it. And as always for more info just look at the docs: https://developer.hashicorp.com/terraform/tutorials/configuration-language/sensitive-variables
