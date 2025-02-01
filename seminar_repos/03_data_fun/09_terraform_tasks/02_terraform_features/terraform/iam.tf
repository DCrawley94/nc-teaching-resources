

variable "colleagues" {
  type    = list(string)
  default = ["fabio", "anna", "yusuf", "hugues"]
}

data "aws_iam_policy_document" "tf_admin_access" {
  statement {
    effect    = "Allow"
    actions   = ["*"]
    resources = ["*"]
  }
}

resource "aws_iam_user" "colleagues" {
  for_each = toset(var.colleagues)
  name     = "${each.key}_tf_admin_access"
}


# resource "aws_iam_user_policy" "admin_access_colleagues" {
#   for_each = aws_iam_user.colleagues

#   name   = "tf-state-access-${each.key}"
#   user   = each.value.name
#   policy = data.aws_iam_policy_document.tf_admin_access.json
# }



