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

Run the `aws configure` command and seen that it wants an access key - to get this lets create a user:

IAM > Users > Create User > Name > AdminAccess (BAD) > Click on user > Create Access Key > CLI access (WARNING: BAD) > copy and past access keys into aws configure

- give admin access + talk about why this is a terrible idea in reality
- mention warning on the top (security risks - we don't want people to get hold of my laptop and have full control over my infrastructure)

Once this is done we can check if its set up correctly using the command `aws sts get-caller-identity`:

> From the docs: Returns details about the IAM user or role whose credentials are used to call the operation.

## First Commands

Get to command reference from the the AWS cli doc page

**HIGHLIGHT THAT WE'RE USING V2 - OFTEN WHEN YOU SEARCH FOR AWS COMMANDS IT WILL GIVE YOU RESULTS FOR V1!!!**

breakdown of initial doc page:

- command structure
- global options
- long list of all available commands

Switch to Figjam and breakdown command

![command structure](./Screenshot%202024-07-15%20at%2015.02.00.png)

e.g: `aws sts get-caller-identity --output json`

---

**PAUSE FOR QUESTIONS**

## Look at some more relevant commands:

- search for s3 with `cmd` + `f`

### Overview of command page:

Look at the s3 command overview page.

- Talk about s3 paths
- Briefly skim over other information
- Look at commands at the bottom and highlight `ls`

### `aws s3 ls`

- differentiate between normal args and parameters
- point out that the basic command is `ls` on it's own or called on a bucket.
- run `aws s3 ls` and compare output to that of console view.

Just like we can take a look at whats in the bucket on the console we can do the same with the cli:

- `aws s3 ls s3://dc-aws-cli-demo`

We can also list things inside nested folders:

- `aws s3 ls s3://dc-aws-cli-demo/more_stuff/`

Or easier we can use the `--recursive` flag to just list everything inside the bucket:

- `aws s3 ls s3://bucket_name --recursive`

Pause for vibe check and highlight the importance of documentation reading for this tool.

- `aws s3 ls s3://bucket_name --recursive --human-readable`

### `aws s3 cp`

Move back to root `s3` page and ask students to try and guess the command that might be useful for copying a remote file down to my local machine.

`cp` like the Unix command

Look at documentation and run the following command:

**This is a good opportunity to show how to run commands on multi lines with backticks**

```sh
aws s3 cp \
  s3://dc-aws-cli-demo/profile.json \
  path/to/save/profile.json
```

Take a look at the contents:

`cat local-file`

## `s3api`

Explain that the `s3` command is useful for general `s3` stuff but if we want more specific stuff we can look at the `s3api` command.

This can be used for more specific commands.

### `get-object-attributes`

Again show `\` for breaking up commands over multiple lines

```sh
aws s3api get-object-attributes \
--bucket "dc-aws-cli-demo" \
--key "profile.json" \
--object-attributes "StorageClass" "ObjectSize"
```

**I'm not sure what this particular command would be used for but it's probably useful to someone!**

**Pause to take questions - give time for typing.**

## `jq`

As we're working in the terminal you might find that you sometimes want to interact or manipulate data like you would in Python.

This would be doable with text manipulation in bash but it would be a massive faff.

Luckily there is a useful tool called `jq` that will make our lives a lot easier.

**Explain that like the aws cli tool, this should have been installed - can check with** `which jq`

Briefly show accessing data from JSON file.

`.` references the json object and from there you can access properties with dot notation and use array indexing like we've seen in python.

```sh
cat profile.json | jq ".name"
cat profile.json | jq ".likes.bands"
cat profile.json | jq ".likes.bands[0]"
```

## End

Take some final questions and round off the session by doing an overview of the learning objectives
