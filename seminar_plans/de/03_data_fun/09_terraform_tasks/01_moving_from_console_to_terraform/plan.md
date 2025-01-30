# Terraform

Figjam: https://www.figma.com/board/GnU9VcCS5mapofQLn8GGrs/Moving-from-the-AWS-Console-to-Terraform?node-id=0-1&t=Lf5Hge7rKMmZqrEa-1

## Learning Objectives

- Solidify our understanding of the relationship between all of the ways we have interacted with AWS so far.
- Understand how the steps we take to deploy infrastructure in the console can be converted into terraform
- Know how to debug terraform errors and navigate the terraform documentation

---

Gonna be like previous seminars. Bit of a partial solution with time spent looking at converting console deployment to terraform deployment.

Maybe spend part of the session walking through a terraform debugging session (create some resources incorrectly and then work through what the errors are telling us?)

## Intro

Get students to remind me what we had to to create an RDS database on Tuesday (emphasise that I don't care about the EC2 security group stuff - just the actual DB creation).

Steps taken (show this on the console):

- choosing engine type
- choosing engine version
- template (not available as terraform is more customised)
- DB identifier
- DB username
- DB password
- everything else DEFAULT

## How can we convert this to terraform?

Ask students to suggest how we could go about finding out how to do this with terraform. I have no idea what resource to use etc.

**GOOGLE: Terraform RDS database** - first result `aws_db_instance`. If you look on the documentation page it has lots of information and even a link to a tutorial. How handy!

Explain that a good approach is to look at the examples and start there.
Looking at the following example ask students to identify things that seem familiar to what we did in the console:

- `engine_type`
- `engine_version`
- `identifier`
- `username`
- `password`

Possibly unfamiliar:

- `allocated_storage` (compare to console and see that this defaulted to 10)
- `db_name` (again you can set this in the console under the additional config header - we didn't set this and just used the default `postgres` db - as terraform states it is optional)
- `instance_class` (another default - can be seen on the RDS creation page in the console)
- `skip_final_snapshot` (mentioned on the DB creation page - defaults to `false`. SPOILER: will need to be `true` if we want to run `terraform destroy`)

Create the RDS db with just the things we know are needed:

**The following will fail when you run apply but this is a good opportunity to do some live debugging with the students**

```tf
resource "aws_db_instance" "rds_example" {
  allocated_storage = 10
  engine            = "postgresql"
  engine_version    = "14.10-R2"
  instance_class    = "db.t3.micro"
  username          = "postgres"
  password          = "password123"
  identifier        = "rds_example"
}
```

Issues with the above:

- `identifier` can only have certain characters in (error output tells you this)
- `engine` should be "postgres" - in the argument reference there is a link to a list of available engines
- `engine_version` should be "14.10" - again in the argument reference there is a link in the docs which can guide you to some documentation. It's a bit of a faff that involves list versions like so: `aws rds describe-db-engine-versions --engine postgres`. This command will give you a list of all the available postgres versions.

After fixing the above run `terraform apply` - this will take ages but you can see a database being initialised on the console while it's running. A great time to pause for questions.

## Next step - do the same but with EC2

Similar to the above but the steps to do EC2.

What did we do in the console to create an ec2 instance?

- Choose OS:

  - Is this something we can do with terraform. No but we can choose a particular ami (copy and paste from browser)

- Choose instance type:

  - `t2.micro`

---

> Create basic EC2 first - none of that security group bullshit:

```tf
resource "aws_instance" "ec2-instance" {
  ami           = "ami-0acc77abdfc7ed5a6" # Copied ami straight from AWS console
  instance_type = "t2.micro"
}
```

> Next: it's `ssh`'in time

We can supply a key like this:

```tf
resource "aws_instance" "ec2-instance" {
  ami           = "ami-0acc77abdfc7ed5a6"
  instance_type = "t2.micro"
  key_name        = "dc-ssh"
}
```

But that isn't quite enough. Can demo what happens when I try to `ssh`.

Hanging - I actually need to allow `ssh` access. How did we do that on the console - take another look at the instance creation menu and see that we created a security group with certain rules.

**Google terraform security group**

See from the docs that there are `ingress` and `egress`. **Get someone to tell me what this means!**

Students will be unfamiliar with:

- `cidr` blocks
- ports (from/to range)
- ip protocol (There is a lot of options for this)

Let's go through the process of setting up an EC2 in the console and seeing what happens to the security group:

**We can see port range, protocol and source** - source doesn't share the name ``cidr` but that is what we want. Let's try:

```tf
resource "aws_instance" "ec2-instance" {
  ami             = "ami-0acc77abdfc7ed5a6" # Copied ami straight from AWS console
  instance_type   = "t2.micro"
  key_name        = "dc-ssh"
  security_groups = [aws_security_group.example-ec2-sg.name]
}


resource "aws_security_group" "example-ec2-sg" {
  name        = "terraform-group"
  description = "Allow ssh traffic to terraform created ec2"
}

resource "aws_vpc_security_group_ingress_rule" "ec2-ssh" {
  security_group_id = aws_security_group.example-ec2-sg.id

  cidr_ipv4   = "0.0.0.0/0"
  from_port   = 22
  ip_protocol = "tcp"
  to_port     = 22
}
```

Now let's try to `ssh` our way in.

## Conclusion

We have successfully converted our knowledge of what we did on the console to terraform configuration 🎉
