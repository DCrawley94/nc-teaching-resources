# Q+A session plan

Server: https://github.com/northcoders/de-sample-server

```txt
DB_PASSWORD: 4]9%nr.Y,:S69EQL
```

Env file:

```sh
DB_HOST=nc-data-eng-production-toy.chpsczt8h1nu.eu-west-2.rds.amazonaws.com
DB_PORT=5432
DB_DB=toy
DB_USER=read_only
DB_PASSWORD=wUg2EXcQcUIa
```

[Solution](https://github.com/data-brain/ec2-deployment-danika/blob/main/day_2_tasks.md)

<ins>Relevant notes:</ins>

[Connecting to remote databases](https://l2c.northcoders.com/courses/de-notes/de2-data-fundamentals-sql#sectionId=connecting_to_remote_databases,step=intro)

[AWS cloud storage and databases](https://l2c.northcoders.com/courses/de-notes/de2-cloud-fundamentals#sectionId=aws_cloud_storage_and_databases,step=intro)

Students are given the option of what they want to focus on from the following choices:

- Recap on RDS and IAM
- How to create an RDS database
- Configuring IAM permissions for EC2/RDS relationship
- Connecting to and seeding an RDS database

## Preparation

Have the following things ready to go:

- An RDS database with Master password set up (no IAM stuff yet)
- An EC2 instance that will be linked - should have a working server using provided `.env` credentials

## Recap on RDS and IAM

Explanations from AWS (a bit sales-y but a good overview)

[IAM](https://aws.amazon.com/iam/)

[What is IAM?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

Use AWS Identity and Access Management (IAM) to manage and scale workload and workforce access securely supporting your agility and innovation in AWS.

When working with AWS it is unwise to have unlimited access to everything - you can have users/roles etc with limited permissions (such as the students account)

[RDS](https://aws.amazon.com/rds/)

[What is RDS?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

Context

As context for why you'd want to configure a connection between your EC2 instance and an RDS database, let's consider the following scenario: Your website presents a form to your users to fill in. You need to capture the form data in a database. You can host your website on an EC2 instance that's been configured as a web server, and you can capture the form data in an RDS database. The EC2 instance and the RDS database need to be connected to each other so that the form data can go from the EC2 instance to the RDS database. This tutorial explains how to configure that connection. Note that this is just one example of a use case for connecting an EC2 instance and an RDS database.

## How to create an RDS database

- Click the **Create Database** button and choose the **Standard Create** option

![RDS Database Creation](./images/rds_db_creation.png 'RDS Database Creation')

- Make sure to choose **PostgreSQL** - **❗NOT AURORA POSTGRESQL❗**

![Postgres version selection and template](./images/postgres_version_selection_and_template.png 'Postgres version selection and template')

- Manually create a master password for the default Postgres user - **Make sure to take note of it for later!**

![Setting RDS credentials](./images/rds_credentials_setting.png 'Setting RDS credentials')

- Leave the rest of the config as the default and click **Create Database** at the bottom of the page

## Configuring IAM permissions for EC2/RDS relationship

**USE PRE-EXISTING DB FOR THIS AS THE DATABASE STATUS NEEDS TO BE AVAILABLE**

For this section I followed this guide: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-ec2-rds-option2.html - you can set up the IAM stuff from the EC2 console instead if you wish.

List of options can be found here: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/tutorial-connect-ec2-instance-to-rds-database.html

**IT IS IMPORTANT YOU WAIT UNTIL THE DATABASE STATUS IS "AVAILABLE" BEFORE YOU DO THIS!**

From the RDS page you can choose to set up a connection with an EC2 instance - this will handle all the steps for you:

- Once the database is created you can scroll down and find the option to set up an EC2 connection

![Creating EC2 connection from RDS](./images/creating_ec2_connection_from_rds.png 'Creating EC2 connection from RDS')

- After clicking on that just choose the EC2 instance that you wish to connect to and click continue. AWS will automatically create some security groups and IAM policies for you.

![Choosing an EC2 instance](./images/choosing_ec2_instance.png 'Choosing an EC2 instance')

**It is good to highlight at this point that by choosing this option you have avoided a lot of manual work that goes into giving permissions for the two service to interact**

## Connecting to and seeding an RDS database

The first step in order to connect to the DB is to get the `psql` command - to do that we will install postgres.

If you run `yum search "postgres"` in your EC2 terminal it will show you all the options you have for installation. This will give you a lot of stuff: postgres modules for different languages and all sorts. The one we want to install is simply called `postgresql15.x86_64`.

!["searching for postgres optons in yum package manager"](./images/yum_search_postgres.png 'searching for postgres optons in yum package manager')

We can install it like so: `sudo dnf install postgresql15.x86_64`

You can confirm it's installed with `psql --version`.

---

Now we have `psql` we're able to connect to the remote database. To connect to the remote DB we need the following info:

- DB username - will be `postgres` if you stuck with the default
- DB password - will be whatever you set the master password to in the first section
- DB Host - can be found on the RDS page for your DB (shown below)
- DB Port - Will default to 5432 so not really necessary (shown below)

!["RDS host url and port number"](./images/RDS_host_url_and_port.png 'RDS host url and port number')

- DB Name - This can be specified in additional config on setup but if yu did not then it will be `postgres` by default. Do not be put off by the empty DB name in the DB config page (shown below)

![RDS config details](./images/RDS_config_details.png 'RDS config details')

---

```txt
PASSWORD: 4]9%nr.Y,:S69EQL
```

You can check that you have the permissions set up correctly by running the following command:

```sh
psql -h "YOUR_HOST_URL_HERE" -U postgres
```

!["Connecting to RDS DB"](./images//connecting_to_rds_db.png 'Connecting to RDS DB')

This will ask you for you the master password which you can provide.

However at this point there is no data in the RDS DB. To seed the database you can use the provided seed script (`src/data/seed.sql`).

You can run the command like so:

```sh
psql -h "YOUR_HOST_URL_HERE" -U postgres -f src/data/seed.sql
```

!["Seeding RDS DB"](./images/seeding_rds_db.png 'Seeding RDS DB')

Once the DB is seeded you should be able to update the `.env` file in the EC2 instance to make you FastAPI use the RDS database that you just created rather than the toy one.

!["New .env file"](./images/new_env_file.png 'New .env file')
