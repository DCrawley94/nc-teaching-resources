## countTheWorlds

Write a function that will find the amount of times the word 'world' is present in a text file.

Your function should use the File System module 'fs' to do this.

The function will take a callback function as an argument and invoke this argument with null and the amount of "world"'s present in the data/helloWorld.txt file represented as an number.

```js
testCB(null, 35);
```

**File Input/Output is blocking code and as such we will be reading the file asynchronously**
