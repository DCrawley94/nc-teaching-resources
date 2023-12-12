# Data Structures - Seminar 1

## Learning Objectives:

- Understand how we can test factory functions with TDD
- Practice applying TDD to object methods
- Understand how to use `this` to access/update an objects properties.

## Introduction

Refresher on differences between Functional and OOP paradigm.

> Ask student for their ideas on these two paradigms in turn

Functional:

- Focus on pure functions
  - avoiding mutation
  - consistent output given a certain input

OOP:

- Focuses on using objects:
  - data is stored as properties
  - behaviours stored as methods (functions)

## Introduce Problem:

You are starting up your own music streaming service to rival Spotify.

Your task is to write a createPlaylist factory function that produces playlist objects for your users to listen to.
Your users should be able to name their playlists, add tracks to it by name, get the name of the current track and move on to the next track in the list.

```js
const partyAnthems = createPlaylist('absolute bangers');

partyAnthems.name; // 'absolute bangers'

partyAnthems.addTrack('superstition');
partyAnthems.addTrack('uptown girl');
partyAnthems.tracks; // ['superstition', 'uptown girl']

partyAnthems.getCurrentTrack(); // `Now playing: superstition`

partyAnthems.nextTrack();
partyAnthems.getCurrentTrack(); // 'uptown girl'
```

## Start Testing

Discuss where to start with the testing:

**Ask students to give examples of behaviours - pick some who chose attributes and ask why they chose this**

- conclusion: testing the simple properties first and then the more complex methods fits our TDD process.

Examples of behaviours:

- returns an object
- object has name property
- object has tracks property

**Possible solution:**

```js
test('playlists have a passed name property', () => {
	const testList = createPlayList('absolute bangers');
	expect(testList.name).toBe('absolute bangers');
});
test('playlists start with an empty tracks array', () => {
	const testList = createPlayList('absolute bangers');
	expect(testList.tracks).toEqual([]);
});

function createPlayList(name) {
	const newList = {};
	newList.name = name;
	newList.tracks = [];
	return newList;
}
```

## Build up tests for methods

**Explain that now we've got the simplest behaviours sorted we can look at the methods**

**Ask for suggestions on tests for the addTrack method**

- addTrack

  - add single track to the list
  - multiple added tracks are remembered

**When crowd sourcing a solution explain that there needs to be some way for the function to refer to an object property - it cannot do this from outside of scope**

**Ask students how it can achieve this**

**`this` is implicitly bound to the current object at the point of invocation**
**the object before the method invocation becomes the value of `this`**

Possible Solution:

```js
test('.addTrack() - adds a passed track to the list', () => {
	// arrange
	const testList = createPlayList('absolute bangers');
	// act
	testList.addTrack('superstition');
	// assert
	expect(testList.tracks).toEqual(['superstition']);
});
test('.addTrack() - adds multiple tracks to the list', () => {
	const testList = createPlayList('absolute bangers');
	testList.addTrack('superstition');
	testList.addTrack('uptown girl');
	expect(testList.tracks).toEqual(['superstition', 'uptown girl']);
});

function createPlayList(name) {
	const newList = {};
	newList.name = name;
	newList.tracks = [];
	newList.currTrackIndex = 0;
	newList.addTrack = addTrack;
	return newList;
}
function addTrack(trackName) {
	this.tracks.push(trackName);
}
```

## Extra methods if there is time:

- getCurrentTrack

  - returns 'Now playing' string
  - test can focus on first song in playlist as nextTrack not implemented yet

`getCurrentTrack` will require them to think of a way of keeping track of which track is currently being played.

Take suggestions for this, a good implementation would be to keep track of the index.

- nextTrack
  - getCurrentTrack now returns next song in playlist
  - this test can use addTrack as it has been tested

**Discussion point: we are trying to test method behaviours, not their implementation - therefore we are not testing for the currentTrackIndex property as this is purely an implementation detail rather than a behaviour**

**if we wanted to refactor our object to track it in a different way (by name for example) then we could still use the same test suite.**

```js
test('.getCurrentTrack() - returns the currently playing track', () => {
	const testList = createPlayList('absolute bangers');
	testList.addTrack('superstition');
	testList.addTrack('uptown girl');
	expect(testList.getCurrentTrack()).toEqual(`Now playing: superstition`);
});

test('.nextTrack() - changes the currentTrack to the next one in the list', () => {
	const testList = createPlayList('absolute bangers');
	testList.addTrack('superstition');
	testList.addTrack('uptown girl');
	testList.nextTrack();
	expect(testList.getCurrentTrack()).toEqual(`Now playing: uptown girl`);
});

function createPlayList(name) {
	const newList = {};
	newList.name = name;
	newList.tracks = [];
	newList.currentTrackIndex = 0;
	newList.addTrack = addTrack;
	newList.getCurrentTrack = getCurrentTrack;
	newList.nextTrack = nextTrack;
	return newList;
}

function addTrack(trackName) {
	this.tracks.push(trackName);
}

function getCurrentTrack() {
	return `Now playing: ${this.tracks[this.currentTrackIndex]}`;
}

function nextTrack() {
	this.currentTrackIndex++;
}
```

## Conclude Session

Talk about how we built up the factory function with TDD

Started with simple tests for properties

Then moved onto methods
