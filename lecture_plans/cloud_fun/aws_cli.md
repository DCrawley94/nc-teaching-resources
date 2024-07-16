# AWS CLI

## Learning Objectives

- Understand when and why we would prefer the CLI over the console
- Understand how to authenticate with the CLI
- Understand the docs and structure of the AWS CLI commands
- Be aware of V1 vs V2
- Know the basic usage of jq for interacting with JSON data on the command line

## Intro

Explain that all the tools we use to create aws infrastructure interact with the AWS api:

- console
- cli
- SDKs - not seen this yet but we will in a couple of weeks

Anything you can do in the console you can do in the CLI

**Ask for suggestions in the chat: Why might we want to use tools like the CLI? - note down ideas on Figjam**

- Automation
- Effiency
- Faster
- Standardisation - less random errors

## CLI Docs intro and CLI user creation

- https://aws.amazon.com/cli/ - students should have it installed

Click into documentation > user guide

Read sales pitch from 1st page

- click into > configure the cli

Highlight that in order to use to CLI we credentials to confirm our identity and permissions

Lot's of options for credentials and config:

- CLI options
- ENV variables
  etc...

**We are gonna use the credentials file** - highlight that this can be created with `aws configure`

We're gonna use an IAM user - click into auth/iam user - mention warning on the top (security risks - we don't want people to get hold of my laptop and have full control over my infrastructure)

---

Create IAM user - give admin access + talk about why this is a terrible idea in reality

- `aws configure`
- `aws sts get-caller-identity` - to check

## First Commands

https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html

- keep in mind that often when you search for specific cli documentation it will give you

---

breakdown of initial doc page:

- command structure
- global options

![command structure](./Screenshot%202024-07-15%20at%2015.02.00.png)

e.g: `aws sts get-caller-identity --output=json`

---

### First example: s3

- search for s3 with `cmd` + `f`

### Overview of command page:

- Talk about s3 paths
- Briefly skim over other information
- Look at commands at the bottom and highlight `ls`

### `aws s3 ls`

- differentiate between normal args and flags
- point out that the basic command is `ls` on it's own or called on a bucket.
- run `aws s3 ls` and compare output to that of console view.
- `aws s3 ls s3://bucket_name`
- `aws s3 ls s3://bucket_name --recursive`

Pause for vibe check and highlight the importance of documentation reading for this tool.

- `aws s3 ls s3://bucket_name --recursive --human-readable`

### `aws s3 cp`

Move back to root `s3` page and ask students to try and guess the command that might be useful for copying a remote file down to my local machine.

`cp` like the Unix command

Look at documentation and run the following command:

`aws s3 cp s3://bucket/key ./local-file.extension`

`cat local-file`

## `s3api`

This can be used for more specific commands.

### `get-object-attributes`

Show `\` for breaking up commands over multiple lines

```sh
aws s3api get-object-attributes \
--bucket "bucket name"
--key "object key"
--object-attributes "StorageClass" "Objectsize"
```

**I'm sure this could be useful to someone**

## `jq`

Pause to take questions - give time for typing.

As we're working in the terminal you might find that you sometimes want to interact or manipulate data like you would in Python.

Briefly show accessing data from JSON file.

## End

Take some final questions and round off the session by doing an overview of the learning objectives
