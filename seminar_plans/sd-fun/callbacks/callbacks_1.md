# Seminar 1: Using response data inside the callback

## Learning Objectives:

- Understand why we must use a callback to access the result of the async process
- Know how to access and manipulate data inside the callback
- know how to pass a resulting value back to user by invoking a given function `cb`

## Introduce the Problem:

**Show this as a markdown preview**

Write a function that will find the amount of times the word 'world' is present in a text file.

Your function should use the File System module 'fs' to do this - **File Input/Output is blocking code and as such we will be doing this asynchronously**

The function will take a callback function as an argument and invoke this argument with null and the amount of "world"'s present in the data/helloWorld.txt file represented as an number.

```js
testCB(null, 35);
```

The function should read this file asynchronously

## Introduce the Repo

Show the students the repo.

Explain that the problem will require the application of some asynchronous code.

In particular highlight the tests - **The students will likely be confused about the tests so focus on the behaviour that they are testing rather than the code**

> Ask if any of the students had looked at the tests and felt confused!

## First Two Tests

Pick Students to help get the first tests passing - **This will not involves FS Readfile yet**

Make a note of the importance of **invoking the given `cb` func** as this allows us **to pass data back to the user**

**Remind students why we need to pass the data to a function and not just return:**

- because this is happening after the synchronous code has run there is nowhere to return it to.
- Instead we can pass it around and use the data for our purposes with functions

Point out that for this function we don't know or care what `cb` does, we just want to pass it the relevant data

We can assume it will just be using the data in some way.

## Final Test

Introduce student to the FS module.

**Important info:**

- gives us a way to interact with our filesystem
- we're going to be using the **callback** api
- point out that some of the methods might seem familiar > `mkdir`, `rm`, `cp`
- highlight the readFile method as the one we'll be using today

**Overview of readFile:**

- up to 3 arguments
- path: file path, if you use a relative path it will be relative to the current working directory (**switch back to VSCode for example**)
- options: a few different options, do go into it in depth now but come back to it later
- callback: a function that will be invoked once the file contents have be retrieved (or possibly not!)

---

Start by asking students for help with calling readFile > **start by using it with just a path and readFile** in order to see what happens.

**log the data that comes back** - explain that the weird buffer object we're seeing is we didn't tell readFile which file encoding to use.

Usually the encoding will be 'utf8', don't worry too much about what this means for now.

---

**at this point highlight that we've dealt with the asynchronous part (`fs`) - we're just dealing with normal logic - it's simply a kata like the ones they've been doing on Wednesday afternoons**

**ask students for some pseudocode to solve the issue of counting substrings**

Hopefully they come to some kind of solution like splitting words, looping and counting OR just use regex 🤷‍♀️

Once we have pseudocode solve problem with assistance of students and get final test working.

Possible Solution:

```js
function countTheWorlds(cb) {
	fs.readFile('./data/helloWorld.txt', 'utf8', (err, data) => {
		if (err) {
			console.log(err);
		} else {
			const worldMatches = data.match(/world/g);

			cb(null, worldMatches.length);
		}
	});
}
```

After the solution talk through how things are working in relation to asyncronicty:

- countTheWorlds goes on the call stack
- fs.readFile is asynchronous to handed off to the Node API
- rest of the code process as normal and stack is cleared
- when asynchronous function is done the callback is added to the task queue
- the event loop checks the call stack and when it's empty the callback is pushed to the stack
- we're now back in synchronous land and can proceed with the logic in the callback
