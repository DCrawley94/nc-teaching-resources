# findNameInFile

Our user wants to see if a given name is present in a particular file that contains a list of characters.

- They want to be able to do this with any name
- The function should be able to search any file

The task is to create a function `findNameInFile` that will be used like so:

```js
findNameInFile('Homer Simpson', './data/simpsons.txt');
```

This function should return a promise that resolves to an object like the one shown here:

```js
{
  searchTerm: "Homer Simpson",
  isInFile: true
}
```

\*if there is some kind of problem with reading the file the user will be happy with a output that shows that the name is not present.
