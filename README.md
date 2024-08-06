# Baboon Hand Labeling Project

This project aims to label baboons in drone footage using the Labelfficient tool. We're organizing our work in batches to make the process more manageable for multiple contributors.

## Getting Started

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution)
- [Git LFS](https://git-lfs.github.com/)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/UCSD-E4E/baboon-hand-labeling.git
   cd baboon-hand-labeling
   ```

2. Install Git LFS and pull the Labelfficient submodule:
   ```
   git lfs install
   git submodule update --init --recursive
   ```

3. Set up the Labelfficient environment:
   Refer to the [Labelfficient README](labelfficient/README.md) for instructions on how to set up the environment.
   Make sure that the active directory is `labelfficient` otherwise you might run into issues.

## Automated Labeling Tasks

We use GitHub Actions to automate the creation of labeling tasks. Here's how it works:

1. A project maintainer creates a new issue with the title format: "Labeling Task: [Video Name] Batch [Number]"
   Example: "Labeling Task: DJI_20230925154521_0008_D_(30s) Batch 2"

2. GitHub Actions will automatically:
   - Create a new branch for this task
   - Create a pull request for the new branch
   - Comment on the issue with a link to the pull request

3. To start labeling:
   - Assign yourself to the issue
   - Go to the pull request linked in the issue
   - Check out the branch locally:
     ```
     git fetch origin
     git checkout labeling-task-[Video-Name]-Batch-[Number]
     ```
   - Pull only the frames for your assigned batch:
     ```
     git lfs pull -I "[Video Name]/batch_[Number]/frames/*"
     ```

4. Label the images using Labelfficient:
   ```
   cd labelfficient
   python gui.py
   ```
   Set the "Dataset:" field to the absolute path of your frames folder, e.g.:
   ```
   C:\Users\username\baboon-hand-labeling\DJI_20230925154521_0008_D_(30s)\batch_2\frames
   ```

5. After completing the batch, commit your changes:
   ```
   git add "[Video Name]/batch_[Number]/frames_Annotations"
   git commit -m "Labeled [Video Name] batch [Number]"
   git push
   ```

6. Go back to the pull request on GitHub:
   - Leave a comment saying you've completed the task
   - A maintainer will review your work and merge the pull request if everything looks good

7. Close the GitHub issue for your completed batch.

## Labeling Guidelines

### What to Label

1. Moving Baboons: 
   - Label baboons that are in a moving position.
   - This includes walking, running, fighting, or climbing.
   - Do not label baboons that are sitting or completely stationary.

2. Other Animals:
   - If you see other animals in the footage, label them as well.
   - Add or use the "other" class name for unidentified animals.
   - Follow the same guidelines as the "baboon" class for labeling other animals.

3. People:
   - If you spot any people in the footage, label them.
   - Add or use the "person" class name for human subjects.
   - Follow the same guidelines as the "baboon" class for labeling people.

### What Not to Label

1. Stationary Baboons:
   - Do not label baboons that are sitting or completely still.

2. Shadows:
   - Do not include shadows in the bounding box.
   - Only label the visible body of the animal or person.

3. Completely Obscured Subjects:
   - If a baboon, other animal, or person is completely hidden behind an object (like a bush), do not label it.
   - Only label subjects that are at least partially visible.

4. Partial Visibility:
   - If part of the subject is visible, create a bounding box around the visible portion only.

### General Tips for Labeling

- Make the bounding box as tight as possible around the subject.
- If unsure about whether to label something, it's better to label it and make a note in your pull request comment.
- Consistency is key. Try to maintain the same criteria for labeling across all frames.

## Tips

- While labeling, it's helpful to open the images in your operating system's gallery application (like Windows "Photos") and flip through them. This allows you to see the full resolution images, as the labeling software compresses them for display.

- Instead of trying to label all baboons on a single frame before moving to the next, it may be easier to focus on one baboon and label it across all frames, then move on to the next baboon. This approach can help you track individual baboons more consistently.

## Acknowledgments

- Thanks to all contributors who are helping with the labeling effort!
- Special thanks to the creators of [Labelfficient](https://github.com/dajes/labelfficient) for providing the labeling tool.