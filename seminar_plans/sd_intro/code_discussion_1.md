# Tuesday Code Discussion

REPO: https://github.com/northcoders/intro-functions/tree/main

Introduction to the practice of sharing code:


Education:
- Clarify your own ideas and understanding 
- Improve your knowledge by seeing work others have done
- Helps you develop skills in assessing and giving feedback to others
- Will give you skills to self-assess and improve your own work

Industry:

- Code Reviews are quite common so get used to sharing the code you write and receiving formative feedback
- Code reviews are an important way to ensure you ship high-quality code and quality software.
- A human who knows your code base can notice code quality issues that automated tests may miss.

My function from intro week January 2021:

**SAVE WITHOUT FORMATTING = CMD + K (don't hold down CMD) > s**

```js
function collectStrings(arr) {

  stringArray = [];
  count = 0;

  while (count < arr.length) {

    if(typeof arr[count] === 'string') {
      stringArray.push(arr[count]);
    }
    
    count++
  }

  return stringArray;
}
```

- Ask students for their thoughts on this - did they do it differently?

- Hopefully someone pipes up and I can ask them to share their code

- If time runs out I can ask them if anyone managed the bonus challenge - ask for suggestions on how this could be done (statement && do something): 
`typeof arr[count] === 'string' && stringArray.push(arr[count])`