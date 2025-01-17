Detective, here are your tasks for the rest of today:

# Introduction

We'll fetch data from the server about Northcoders employees and store it locally.

## Challenges

### Task 1

Write a function called `get_people` that will retrieve list of all the available people on the `northcoders` server . This should:

1. Use the [`requests`](https://pypi.org/project/requests/) module to make a request to `https://nc-leaks.herokuapp.com/api/people`.
2. Once you have the response body as a useable dictionary, look through the people to find anyone who has `northcoders` as the workplace.
3. Save these `northcoders` employees to a file called `northcoders.json`.

### Task 2

Write a function called `get_interests` that uses the newly found usernames for each northcoder to retrieve information on everyone's interests. This function should:

1. Read the `northcoders.json` file you created in task 1
2. For every person, use their `username` and make a request to `https://nc-leaks.herokuapp.com/api/people/:username/interests` to get their interests.
3. Each response will be a JSON with a person key. Collect up the data on this `person` key into a list.
4. Once you have all responses in the list, save it to a file called `interests.json`.

### Task 3

Write a function called `get_pets` that does the same as the Task 2 but for pets. The endpoint is `https://nc-leaks.herokuapp.com/api/people/:username/pets`;

> Note: Some of the users do not have pets and so the server will give a 404 response! These responses should not be included in the `pets.json`. Consider how to you will use the status code to inform when to include some pets.

### Task 4

Automation is great. Create a function called `scavenge_for_nc_data` that uses all of the functions you created in Tasks 1-3 to automate your hunt for data.

## Additional Challenges

Well done for getting this far Detective! Now you've completed the core tasks, you should broaden the scope of this investigation by making requests to other servers.

You should firstly take some time to read the documentation for your chosen API and try out various requests to see what response data you can get. Then, create some functions similar to the ones in previous tasks, based around the ideas of:

- Requesting and storing data
- Filtering data according to some criteria
- Collating data from multiple requests

You can choose any API you would like but bear in mind that not every single one will let you access their servers for free. Here are some suggestions for publicly available APIs:

- [PokeAPI](https://pokeapi.co/) - Pokemon data
- [The Cat API](https://thecatapi.com/) - Cat data
- [TV Maze](https://www.tvmaze.com/api) - TV Show data
- [Google Books](https://developers.google.com/books/docs/overview) - Book data

There is also this handy list of [public APIs](https://github.com/public-apis/public-apis) that you can browse.

**Note**: some of these servers may require you to sign-up first in order to request an API key which you can then use as part of the requests you make. Be aware of this requirement, and if you don't wish to sign-up then you can choose one of the APIs that does not require a key (e.g. the PokeAPI).