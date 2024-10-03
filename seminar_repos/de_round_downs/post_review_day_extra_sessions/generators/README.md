# Generators - indexer

Write a generator called `indexer` that indexes the words in a piece of text by
returning the position of the first letter of each word (zero-indexed).
For this exercise, words are delimited by spaces, tabs, or new lines.

**This task must be completed with a Generator!**

The tests are pre-written. Remove the `skip` decorators to run them.

**Do not change the pre-written tests!**

Examples:

```bash
text1 = "The name's Copley, Paul Copley."
result1 = indexer(text1)
list(result1)
[0, 4, 11, 19, 24]

text2 = 'Vive la France!'
result2 = indexer(text2)
next(result2)
0
next(result2)
5
next(result2)
8
next(result2)
StopIteration

text3 = """The
End"""
result3 = indexer(text3)
list(result3) == [0, 4]

with open('sonnet18.txt', 'r') as f:
    text4 = f.read()
    # Shall I compare thee to...
    result4 = indexer(text4)
    print(next(result4)) # 0
    print(next(result4)) # 6
    print(next(result4)) # 8
```
