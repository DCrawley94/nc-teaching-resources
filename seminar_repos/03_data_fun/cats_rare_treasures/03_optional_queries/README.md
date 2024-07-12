# Integration Testing with Fastapi

## Usage:

- install requirements from txt file
- run `psql -f db/db-setup/sql` to create the `nc_games` database
- update `db/connection.py` file to use your Postgres username
- run `python db/run-seed.py` to seed the DB

## Notes

Recommended flow:

- have test for `/api/reviews` pre-written
- test `/api/reviews?sort_by=rating` to introduce optional query (default to DESC order)
- test `/api/reviews?sort_by=username&order=ASC` to make order programmatic

- Can then take a break talk about what could go wrong:

  - dodgy sort_by/order values
  - risk of sql injection

- Move onto tests for bad query requests and bring in Pydantic Union types

Stuff about literals/keywords:

- [PG8000 docs](https://github.com/tlocke/pg8000?tab=readme-ov-file#many-sql-statements-cant-be-parameterized)
- Column names are identifiers and therefore can't be parameterised
- ASC/DESC are keywords and therefore can't be parameterised either
- [Postgres docs on identifiers/keywords](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS)
- [List of Postgres keywords](https://www.postgresql.org/docs/current/sql-keywords-appendix.html)

---

I've not included dotenv but you may want to briefly go over it at the start of the seminar as a refresher
