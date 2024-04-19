`shell` function is command expansion

Nice way to print vars - can be done anywhere:

```make
$(info $$SHELL is [${SHELL}])

yeet:
  @echo "get fucked"
```
