


# Eventloop Api

This project aims to ease the booking of event centre. To contribute, follow the steps below.

## Fork this repository

This will create a local copy of the repository in your GitHub account
![image](https://user-images.githubusercontent.com/95700260/192919803-ccdc8fa2-6549-40f7-9b3f-cf57a43ac019.png)

## Clone the repository

![image](https://user-images.githubusercontent.com/95700260/192920005-0db4bf7a-0dbd-45bd-b9cd-ada99d6169e7.png)

Now clone the forked repository to your machine. Go to your GitHub account, open the forked repository, click on the code button and then click the _copy to clipboard_ icon.

Open a terminal and run the following git command:

```sh
git clone <url-you-copied>
```

where `<url-you-copied>` is the url to this repository (your fork of this project). See the previous steps to obtain the url.

For example:

```sh
git clone https://github.com/olakayCoder1/eventloop.git
```

## Make a branch

Change into the repository directory on your computer (if you are not already there):

```sh
cd eventloop
```

Keep a reference to the original project by entering the following command:

```sh
git remote add upstream https://github.com/olakayCoder1/eventloop.git
```

Create a new branch that describes the changes that you're going to make. For example, to create a branch named "authentication-implementation", enter the following command:

```sh
git branch authentication-implementation
```

Switch to the branch by entering `git checkout <name-of-branch>`. For our example, the command will be:

```sh
git checkout authentication-implementation
```

## Make changes and commit the changes



## Push changes to GitHub

Push your changes using the command `git push`:

```sh
git push origin -u <your-branch-name>
```
replacing `<add-your-branch-name>` with the name of the branch you created earlier.

As per our example, the command will be:

```sh
git push origin -u authentication-implementation
```

## Submit your changes for review

Open your forked repository on GitHub. Click on the `Compare & pull request` button.


Create a pull request


And that's it! Your Pull Request has been submitted! You will get a notification email once the changes have been merged.


<details>



> Please read further if you have any conflicts or your pull request refuses to go through.


<summary> <strong>A note on resolving merge conflicts</strong> </summary>

> Read the GitHub docs about resolving merge conflicts [here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts).

To avoid fixing merge conflicts, all changes made will have to be discarded.

To get started, sync your forked repository by going to the GitHub page, then click the `sync fork` button. 

Next, discard your commits.

![Screenshot of GitHub repository with the link to sync fork highlighted](https://i.ibb.co/C15MDjR/syncfork.png)

Then make a fresh clone of your newly synced repository and follow the steps from [Clone the repository](#clone-the-repository).

</details>

