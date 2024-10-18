data "aws_iam_policy_document" "tf-admin-access" {
  statement {
    effect    = "Allow"
    actions   = ["*"]
    resources = ["*"]
  }
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
