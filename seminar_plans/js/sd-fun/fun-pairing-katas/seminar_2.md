# Seminar plan

## Learning Objectives:

- Develop our understanding of TDD
- Understand how our code works in reference to the Execution Context

**ZOOM CHAT PRIVATE: CHAT WINDOW > THREE DOTS > PARTICIPANT CAN CHAT WITH HOST AND CO-HOST**

## Intro: FigJam

https://www.figma.com/file/G0tJZ9jx3uUUOzreYUEljY/Fun-Pairing-Sem-2?type=whiteboard&node-id=0%3A1&t=F8B6SJ6ELNQDrMQ1-1

Introduce the problem:

- The function getMiddleChar should return the middle character of a string. If the string is of even length, return the middle two characters.
- It should ignore any whitespace and special characters.

  > E.g. 'hello' should return 'l'

  > 'code' should return 'od'

  > 'hello world' should return 'ow'

  > 'nor?thc.o,de!rs' should return 'c'

---

**🏁 CHECKPOINT 🏁**

---

**SWITCH TO VSCODE**

Explain that the function is currently in a semi-complete state:

- two tests
- code written to pass first test, I have identified second behaviour to test

Simplest behaviours being tested:

- empty string/ single character/ two character. Behaviour: less than length of 3 = return string
- odd length string >= 3

**POINT OUT THAT I'M USING toBe INSTEAD OF toEqual, IS THIS OKAY AND WHY?**

**RUN TESTS**

We will now be working towards a solution 👯‍♂️

## Test 1:

**Warmup exercise: pick someone to suggest a possible solution to pass test**

> ✨pseudocode✨

🧑‍🎓 Ask for a volunteer or pick on someone to identify the next possible test - increase in complexity 🧑‍🎓

> 🧑‍🎓 ask for explanation 🧑‍🎓

**Hopefully they pick even length string - no whitespace/punctuation**

> 🧑‍🎓 If not have a vote to see if it would be easier to start with a simpler test case 🧑‍🎓

🧑‍🎓 Ask someone else to talk me through how they'd write this test 🧑‍🎓

Ask for suggestions of the **VERY FIRST THING WE DO AFTER WRITING A TEST**

✨ _see it fail_ ✨

---

**🏁 CHECKPOINT 🏁**

---

## Execution Context Time

Explain that while I know that many of them could give me a solution straight away we're going to use our knowledge of how JS executes to solve the problem.

**CMD - CTRL - SHIFT - 4** (to screenshot and copy to clipboard)

Bring up FigJam with an execution context diagram.

Get students to help me fill it out for the given function invo with prompts:

- What's the first thing that happens? (global)
- Next thing (function invo) - **Mention that JEST etc. will be on the stack but we won't be concerned with it as we're focusing on the code we are writing**
- What happens in the thread/VE whe the function is invoked?
  - VE: str ('code')
  - conditional check
    - evaluate condition
    - false: continue down
  - middleIndex is index 2 - therefore 4rd character is returned
    **BOOM - WE SOLVED IT**

**CHECKPOINT - DO STUDENTS UNDERSTAND WHAT WE HAVE BEEN TALKING ABOUT**

> Point out that we don't expect them to write out a whole diagram for every problem BUT it can be helpful to take the time to understand the code you're writing and looking at how it executes for a given argument.

## Solution

Ask for a volunteer to describe how they'd solve it - write pseudocode.

For example:

```js
// create variable to hold the middle index
// use that to return the middle char
```

Throw back to talking about the Execution Context and ask studes what will be held in the variable environment and what is going to happen on the thread.

Ask someone to walk me through a solution

**Possible Solution:**

```js
function getMiddleChar(str) {
	// UNNEEDED:
	// if (str.length < 3) {
	// 	return str;
	// }

	const midIndex = Math.floor(str.length / 2);

	if (str.length % 2 === 0) {
		return str[midIndex - 1] + str[midIndex];
	}

	return str[midIndex];
}
```

---

**🏁 CHECKPOINT 🏁**

---

## Next Steps:

Ask for a volunteer to suggest a new test

- Whitespace
- Punctuation

**Both a good excuse to show of `str.replace`**

> For each test first ask for someone to talk through why it's not working - each time refer back to Variable Environment and what is happening in the thread
