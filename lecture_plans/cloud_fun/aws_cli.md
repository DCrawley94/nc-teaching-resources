# AWS CLI

## Intro

- Comparison to Console usage
- Why use CLI

## CLI Docs intro and CLI user creation

- https://aws.amazon.com/cli/ - students should have it installed

Click into documentation > configure the cli

Lot's of options - we are gonna use to credentials file

We're gonna use an IAM user - click into auth/iam user - mention warning on the top (security risks - we don't want people to get hold of my laptop and have full control over my infrastructure)

---

Create IAM user - give admin access + talk about why this is a terrible idea in reality

- `aws configure`
- `aws sts get-caller-identity` - to check
