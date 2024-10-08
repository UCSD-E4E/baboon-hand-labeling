# Baboon Hand Labeling Project

This project aims to label baboons in drone footage using the Labelfficient tool. We're organizing our work in batches to make the process more manageable for multiple contributors.

## Getting Started

### Prerequisites

- [Anaconda](https://www.anaconda.com/products/distribution)

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/UCSD-E4E/baboon-hand-labeling.git
   cd baboon-hand-labeling
   git submodule update --init --recursive
   ```

2. Set up the Labelfficient environment:
   Refer to the [Labelfficient README](https://github.com/dajes/labelfficient/blob/ca4b00f5f95ed206f488c95f5068b38570903aab/README.md) for instructions on how to set up the environment.
   Make sure that the active directory is `labelfficient` otherwise you might run into issues.

## Labeling Process

1. Create a new branch for your assigned batch and immediately publish it:
   ```
   git checkout -b "labeling-task-[Video-Name]-Batch-[Number]"
   git push -u origin "labeling-task-[Video-Name]-Batch-[Number]"
   ```

2. Locate the "labeling_share/baboon-hand-labeling" folder in the root of the NAS. It has a similar folder structure to this repository.

3. Find the zip file corresponding to your assigned batch in the NAS folder structure.

4. Download the zip file and place it in the same relative folder within your cloned repository.

5. Unzip the file in place.

6. Label the images using Labelfficient:
   ```
   cd labelfficient
   python gui.py
   ```
   Set the "Dataset:" field to the absolute path of your frames folder, e.g.:
   ```
   C:\Users\username\baboon-hand-labeling\DJI_20230925154521_0008_D_(30s)\batch_2\frames
   ```

7. After completing the batch, commit your changes:
   ```
   git add "[Video Name]/batch_[Number]/frames_Annotations"
   git commit -m "Labeled [Video Name] batch [Number]"
   git push
   ```

8. Create a pull request on GitHub for your completed batch.

9. A maintainer will review your work and merge the pull request if everything looks good.

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

- While labeling, it's helpful to open the images in your operating system's gallery application (like Windows "Photos") and flip through them. This allows you to see the full resolution images, as the labeling software compresses them for display.
- Instead of trying to label all baboons on a single frame before moving to the next, it may be easier to focus on one baboon and label it across all frames, then move on to the next baboon. This approach can help you track individual baboons more consistently.

## Acknowledgments

- Thanks to all contributors who are helping with the labeling effort!
- Special thanks to the creators of [Labelfficient](https://github.com/dajes/labelfficient) for providing the labeling tool.
