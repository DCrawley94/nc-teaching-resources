# Thursday Code Discussion

Look at the advanced problem solving challenges and treat it as a mob debugging sessions.

Work through advanced exercises and break down the errors to really hammer home how helpful the stack traces are.

E.g.

```sh
shoutNames should return an array of one name with "!" on the end
 ReferenceError: word is not defined
    at /Users/danika/nc/teaching/seminar_repos/sd_intro/code_discussion_3/debugging/advanced/1.debugMeAdvanced.js:5:5
    at Array.forEach (<anonymous>)
    at shoutNames (/Users/danika/nc/teaching/seminar_repos/sd_intro/code_discussion_3/debugging/advanced/1.debugMeAdvanced.js:4:30)
    at /Users/danika/nc/teaching/seminar_repos/sd_intro/code_discussion_3/debugging/advanced/1.debugMeAdvanced.js:19:11
    at runTest (/Users/danika/nc/teaching/seminar_repos/sd_intro/code_discussion_3/test-api/index.js:60:5)
    at Object.<anonymous> (/Users/danika/nc/teaching/seminar_repos/sd_intro/code_discussion_3/debugging/advanced/1.debugMeAdvanced.js:16:1)
    at Module._compile (node:internal/modules/cjs/loader:1198:14)
    at Object.Module._extensions..js (node:internal/modules/cjs/loader:1252:10)
    at Module.load (node:internal/modules/cjs/loader:1076:32)
    at Function.Module._load (node:internal/modules/cjs/loader:911:12)
```

Pick on people to ask what they think is the reason for certain errors etc.

---

Advanced task 1:

**before running file be clear that we're going to be looking predominantly at the output, I don't just want solutions I want to pick out the useful information and take it from there**

- run file and ask students to look at the output.

> What in particular stands out?

- Word undefined
- Returning undefined

---

Advanced task 2:

Run test and point out that in this case there's no obvious error in the terminal that we can use for debugging.

We have to trace down what is happening.

**Talk about how it can be helpful to trace the path through the code and log things**
**e.g. log the bank account in the loop - skip other tests**
**hmm no log appearing, why might this be? We can see one before and after the loop?**
**In this case the loop is set up wrong so the loop body never runs - watch out for things like this and think about how you can check your code is working correctly**

---

Advanced task 3 + 4:

Similar to two but pick students to lead me through the steps we could take to debug:

- something is undefined - lets trace it down

---

If time try task 5

**Highlight how this is starting to get trickier now we're dealing with longer sections of code**

- not much context for this function
- questionable/unclear documentation
- before even starting to debug the issue we need to spend a lot of time reading and understanding exactly what is going on here - this is a skill that will take time to develop
