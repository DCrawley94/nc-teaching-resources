# Git: Distributed Version Control

## Recap

This morning we saw the benefits of using version control to keep a timeline of changes for projects that you're working on.

We saw:

- Initialising a project as a git repository with the command: `git init`
- Adding changes to the staging are with the command: `git add`
- A snapshot (otherwise known as a commit) including the new changes was added to the timeline with the `git commit` command.

> Ask is everyone is onboard with those concepts before moving on

## Benefits of storing a project remotely

Talk about benefits of storing a project remotely (somewhere other than the local machine) rather than locally.

Remotely:

- Project isn't lost if the machine breaks (reference water damaged macbook)
- Accessible by others (multiple collaborators on a single project)

## Demo:

Use this repo: https://github.com/DCrawley94/example-git-repo

All that's been done is creating a completely empty repo.

Show the instructions on how to link up the local repo.

Walk through the instructions:

`git remote add origin`
`git branch -M main` - used for renaming an old branch, don't need to worry about this too much as the branch is already called main
`git push origin main`

Show that the repo is now available on Github.

**Once this is done ask helper to make some kind of change.**

Show how to add collaborators: settings > access > collaborators. This sends the person an email asking them to join which they have to accept. They can then access and make changes etc.

After this time a change should be made that we can see on the main page.

In local repo show have remote changes can be pulled down.

**Diagram Time: https://www.figma.com/file/pEibDwx7JHG88TMy5xJxvd/Git-Distributed-Version-Control?type=whiteboard&node-id=2-37&t=CPx7XFdV27LJniUn-0**

Break down **`git push origin main`**

| git                | push   | origin      | main        |
| ------------------ | ------ | ----------- | ----------- |
| Main `git` command | action | remote name | branch name |

Finish Up and tell students they will be paired up for some git tasks
