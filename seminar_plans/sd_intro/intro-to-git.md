# Lecture Outline

1. Introduce the concept of version control - what is it and why should we use it ?
2. Introduce a conceptual model for understanding how Git works - working directory, staging area and git repository
3. Introduce some of the fundamental git commands and how they fit into the conceptual model above - `git add`, `git commit`

## Reason for version control:

Instead of multiple files representing multiple different versions, what if there was a way to keep track of the changes to a file (or multiple files) over time.

## Why Version Control is important:

Let's take a theoretical large codebase such as for an app like Spotify.

It has tons of features like:

- creating and account
- searching for songs/artists
- creating playlists

I want to add a new feature:

- I want a feature that lets me hum a tune and find songs that sound like that.

> What could go wrong.

Hopefully students will provide answers such as **breaking previous features**

This should lead nicely into the next section:

## Benefits of Version Control

Version control gives the following benefits:

- Ability to roll back to a **previous version** if something is broken.
- Keep a history/timeline of changes - again useful for rolling back to working versions
- Allows for collaboration. This will be discussed more this afternoon.

## Git: A concept

### A timeline of snapshots

We use version control to essentially create a timeline of snapshots.

These snapshots will persist in the Git repository (A repository is simply a place that you can store your code) or in the `.git` directory. - More on these things soon.

Git will track any change in the working directory (the files or directories that are currently viewable - where this be in VSCode or another editor). Any modifications to those files will only take place in the working directory - they are not saved as a snapshot on the timeline unless we do so explicitly.

If we decide to keep the change we've made we can add them to the **staging area**, this is like a waiting room.

Finally if I create the snapshot and add those changes to my timeline, the snapshot is added to the `.git` directory I spoke about earlier.

## Example

- Create a new repo

- Git init - then ls -a to show created `.git` directory. Can do an `ls` as a bit of a gotcha.

- Run `git log` - fatal no commits found. Explain that commits is the word for a snapshot.

- Create a snapshot: Create file > write to file > save file > `git status` > `git log` > `git commit -m` > `git status` > `git log` > 👏 FIN 👏

## WInd down

Wind down session, ask for Qs etc.
