

data "aws_iam_policy_document" "tf-admin-access" {
  statement {
    effect    = "Allow"
    actions   = ["*"]
    resources = ["*"]
  }
}


# resource "aws_iam_user" "colleagues" {
#   #   for_each = toset(var.colleagues)
#   name = "jenny"
# }

# resource "aws_iam_user_policy" "tf-admin-access" {
#   #   for_each = toset(var.colleagues)

#   name   = "geoff_tf_admin_access"
#   user   = aws_iam_user.colleagues.name
#   policy = data.aws_iam_policy_document.tf-admin-access.json
# }

