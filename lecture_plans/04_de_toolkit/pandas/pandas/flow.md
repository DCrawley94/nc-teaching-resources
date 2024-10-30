# Wrangling with Pandas 🐼

## Learning Objectives

- Understand the purpose of the pandas library
- Create and manipulate series in pandas
- Create and manipulate data frames within pandas
- Use pandas to read & write files
- Understand the benefit of storing data in parquet format
- Create a parquet file
- Use a jupyter notebook as our testing ground

## 1. Why pandas?

- Pandas is a library that is widely used by data scientists/engineers
- The primary object within pandas is called a "data frame", and we're going to get familiar with this because it's used not only in pandas but other libraries like Spark
- They are used a lot!
- We are going to be doing lots of data manipulation with pandas including between file types

Can't we do this already?

- Yes, in a few ways:
  1. [Data in a database] Use SQL to interact directly with a database
  2. [Data in files] Use SQL + metadata
  3. [Data in files] Use a tool like pandas

## 2. What is pandas?

> From the docs: "fast, powerful, flexible and easy to use open source data analysis and manipulation tool, built on top of the python programming language"

- We will be doing data manipulations like:
  - **Cleaning, checking** - checking over data that is perhaps incorrectly formatted or has missing values
  - **Queries, filters**
  - **Calculations, analysis** - what data scientists do
  - **Reformatting, remodelling**

## 3. Set up jupyter and whatnot

- `python -m venv venv`
- Go into repo, `pip install jupyterlab` - a familiar tool but you're going to be using it during the sprint
- `pip install pandas`
- Once the installing is done... run `jupyter lab` and see it in browser

## 4. Intro `pandas` with `Series`

### Intro

- We can construct one from a list
- It has a squillion methods available, you will use some
- If we execute it we can see they are indexed values also with `dtype` (a data type)
- `s1.values` is a **`numpy` array** - the whole library is built on top of `numpy` which itself allows for lots of coooool mathsy stuff

### What you can do

- You can do a whole lot of stuff like:

  - Indexing
  - Slicing
  - Multiply things by a number
  - Calculate averages
  - Filter using `s1.where(s1 > 10)` (maintains the failing parts)
  - Filter using slicing `s1[s1 > 10]` (removes the fails)

- You can also explicitly declare the index
- Or you can create it from a dictionary
  - _Note:_ you can also slice one created from a dictionary!
  - If you do this, it actually _includes_ the end index for whatever reason

## 5. Framing data with dataframes

### Intro

- Dataframes are 2-dimensional - they are effectively tables
- You can form a dataframe from two series

### What you can do

- On the table:

  - View the table
  - Look at the `dtypes`, the `columns`, and the `values`
  - _Also_ the column names themselves actually become attributes

- On the columns:

  - Access and manipulate columns (the columns are themselves just series, after all)
  - Create new columns using operations like `frame['c'] = frame['a'] * frame['b']`

- Use `.loc[]` to do a bunch of weird shit
  - Use it to slice across columns
  - Get individual values according to column and row
  - So many other things
  - Also there `iloc[]` if you want to do it numerically

## 6. File reader? I barely know her!

- We can read and write files using `pandas` also

  - We can do this with Python obvs, but this folds into dataframes naturally
  - Makes it very pleasant to convert between file types

- Let's create a dataframe from a CSV I have right here

  - I'm going to ignore any errors, like some emoji it can't interpret

- Now in reality, we might have a shit load of data so won't just look at it all right away so instead get `count` or `head`
- Now I've got it, I can apply SQL-like queries to that dataframe

## 7. File conversion

- Use `pandas` to convert the CSV into a JSON file as an initial example
- Introduce the parquet format and motivate it
  - Discuss what it means to have columnar data and its efficiency
  - Columnar data allows us to discard a bunch of data, rather than having to read in every single row
  - Parquet is a binary file with its own metadata encoded into it (meaning avoiding of inconsistency)
  - It's also optimised for columnar read processes, and for these two reasons it's better than just doing columnar JSON
- **Remember** - install some extra dependencies needed for parquet `pip install pyarrow`
- We can view the binary file and it looks like nonsense, but install `parquet-tools` and you can view it nicely

```bash
parquet-tools inspect file.parquet | more
```

## 8. Conclusion

- That's everything - not a better or worse way to do things than using SQL, just appropriate for different circumstances
- Jupyter is not tied with `pandas` but Data Scientists will often use it for prototyping

**NOTE** - the markdown data in the sprint does _not need to be read in programmatically._ You can just copy and paste or type it out or whatever
