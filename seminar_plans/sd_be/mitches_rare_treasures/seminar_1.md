# Environment Variables - Seminar 1

`package.json` scripts at the start:

```json
"scripts": {
		"setup-db": "psql -f ./db/db-setup.sql",
		"seed": "PGDATABASE=nc_games node db/run-seed.js",
		"test": "PGDATABASE=nc_games jest",
		"dev": "nodemon listen.js"
	},
```

## Intro

In the lecture we introduced the idea of separate versions of a database for testing/development/production.

Ask students to suggest why we might want to use separate databases.

**XYZ, give me one reason why I might want a separate DB for testing etc...**

Note down some of these reasons

**possible reasons:**

```txt
- Separate testing DB allows us to regularly re-seed and test our endpoints without breaking other tests

- We would not want to run tests using a live database - things can go wrong and we wouldn't want to delete customer data for example

- In regard to another DB - development - maybe we're building an application which queries our database and we want a more realistic DB for that. One that isn't constantly being re-seeded and reflects any update. However as it's still for development purposes (and things can go wrong) we don't want to use the production DB
```

Finish up this section by saying that ideally we want different databases that can be used in different scenarios.

## Previous use of ENV variables

**Ask students how we have previously made use of environment variables to set the DB that we're using**

- `PGDATABASE`

**Show running the `npm run seed` script with `PGDATABASE` present.**

If this environment variable is present then this is the Database that Node Postgres will connect to.

If it's not there it will try and connect to the default database which is something we don't want.

**Explain that this has been okay up until this point - however this is quite manual - also it leaves information exposed to anyone who might come and look at our code on Github**

**Ask students if they can think of any reasons why we might not want to expose environment variables directly like this**

- might need to have sensitive information in the environment. E.g passwords/other sensitive information about databases etc.

**How could we avoid exposing data like this in our code?**

- ✨ dotenv ✨

**remove PGDATABASE environment variable from package.json scripts** - mention that this will cause errors until we come up with a solution with dotenv

New scripts:

```json
"scripts": {
		"setup-db": "psql -f ./db/db-setup.sql",
		"seed": "node db/run-seed.js",
		"test": "jest",
		"dev": "nodemon listen.js"
	},
```

## Using dotenv

Ask students how we would use the `dotenv` package.

Create files that start with `.env`, the dotenv.config method will read variables from those files and store them on the `process.env` object as a key-value pair.

e.g.

```sh
# .env

PGDATABASE=nc_games
```

However in this session I intend to make use of two separate database.

A test one and a development one.

So we're going to use two separate `.env` files to make sure that the appropriate DB is used at the right time.

```sh
# .env.development

PGDATABASE=nc_games
```

```sh
# .env.test

PGDATABASE=nc_games_test
```

Now I'm going to set up the connection file to use `dotenv` in order to make sure the right PGDATABASE environment variable is being set.

### NODE_ENV

Talk about how we can do this by making use of a commonly use environment variable.

Often used in development of `node` projects is an environment variable called `NODE_ENV`.

In fact the Jest testing library knows that it is commonly used and will set it to have the value of 'test' for us. It does this for free, how kind!

**Log process.env.NODE_ENV in connection.js and run tests**

**Show that if the file is run normally it is undefined** - node db/connection.js

Therefore we can direct `dotenv` to read in the PGDATABASE using that value.

**Show how I can access the NODE_ENV and use it to read `.env.test file`:**

```js
const ENV = process.env.NODE_ENV;
const pathToCorrectEnvFile = `${__dirname}/../.env.${ENV}`;

require('dotenv').config({
	path: pathToCorrectEnvFile
});

console.log(process.env.PGDATABASE);
```

**Talk about the fact that the db connection could be required anywhere I want to ensure the file path will work regardless - therefore I use \_\_dirname**

**\_\_dirname is a global `node` variable that stores the directory name of the current module** - point people to the docs/notes if they want to find out more about this

- it allows us to create an absolute path to the correct .env file and allows the file to be run from anywhere in the repo
- throwback to path issues when using `fs` - this is a way to avoid those kind of issues.

**Show this working again when I run tests - but still breaking when I run seed**

---

Speaking of the seed, show how the test file is seeding the database with test data before each test.

Talk about how I now want the `run-seed` to just have the job of seeding development data only!

**change import to import the dev data**

**change filename to be `seed-dev` instead**

**update package.json - change script name and the file it runs**

---

SHORT BREAK to tak a breathe and ask students to think about what we've done so far:

- changed it so the environment variables are stored in `.env` files that can be git ignored
- updated the connection file to connect to the **test database** if `NODE_ENV` is set to **'test'** - however we still haven't handled the **development database** ... YET
- We have seen that the test database is being seeded before each test and the tests should still be passing.
- `seed-dev` command is still failing due to lack of PGDATABASE environment variable

---

How can we fix this to work for the `development` env file and ensure we connect to the development DB when we want to?

Currently the only options ar either `test` or `development`. So we can assume if there's no NODE_ENV environment variable set then we should be using the development DB.

Therefore I can change the variable assignment slightly like so:

```js
const ENV = process.env.NODE_ENV || 'development';
```

**log the above and show it working for tests and running file directly**

## Prove this works

It's all well and good showing you this but I want to prove that it works.

Log result of get all games in test file and show that it is only 3 games.

Run `npm run dev` and make a request through insomnia and show that it's getting more games

**can we see how we're forcing node postgres to connect to the appropriate DB with our use of the PGDATABASE variable?**

## Listen

While we talking about Insomnia can anyone tell me why we need to extract the `app.listen` to it's own file?

- Testing packages for our back-end apps will establish their own listeners - this will not work if listening happens as part of the app definition.

- In order to test our back-end apps properly, we will need to extract this functionality to a separate file.

Show what happens if I put a listen in the app.js and run tests - the connection is still hanging!

## Finish off and take questions
