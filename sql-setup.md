# Postgres Check/Setup

## Mac

- Install Postgres App https://postgresapp.com/
  - Open the app (little blue elephant) and select initialize/start
- type `psql` into your terminal. You should then see something similar to:

```psql
psql (14.11 (Homebrew))
Type "help" for help.

username=#
```

- if the above does not show/you get an error, run the following commands in your terminal:

  - `brew update`
  - `brew doctor`

- If you see the following error: _`psql: error: connection to server on socket "/tmp/.s.PGSQL.5432" failed: FATAL:  database "username" does not exist`_, then run the command _`createdb`_ to initialise the database.

## Ubuntu / WSL

**In your linux terminal:**

- Run this command to enter the terminal application for PostgreSQL:

  `psql`

You should see something similar to this:

```psql
psql (14.9 (Ubuntu 14.9-0ubuntu0.22.04.1))
Type "help" for help.

danika=#
```

If you see the following error:

```sh
psql: error: connection to server on socket "/var/run/postgresql/.s.PGSQL.5432" failed: No such file or directory
        Is the server running locally and accepting connections on that socket?

```

Please run `sudo service postgresql start` to ensure that the postgresql server is running before trying the above again.

The next step is to create a password for you Postgres user.

**Please make sure you take note of the password as you'll need it later on**.

- Now type:

  `ALTER USER username WITH PASSWORD 'mysecretword123';`

  **BUT** Instead of `username` type your Ubuntu username and instead of `'mysecretword123'` choose your own password and be sure to wrap it in quotation marks. **Please don't forget the semicolon and the end, this is important!**. Use a simple password like 'password'. **DONT USE YOUR LOGIN PASSWORD** ! You should see the response `ALTER ROLE` after you have run the command. If you don't see that, you may have forgotten the semicolon at the end. Please run the `ALTER USER` command again with the semi colon at the end.

- Once you see `ALTER ROLE` in the terminal, you can then exit out of psql by typing `\q`
