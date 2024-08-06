---
name: Labeling Task
about: Create a new labeling task for a batch of images
title: 'Labeling Task: [Video Name] Batch [Number]'
labels: labeling
assignees: ''

---

## Labeling Task Details

**Video Name:** [e.g., DJI_20230925154521_0008_D_(30s)]
**Batch Number:** [e.g., 2]

## Instructions for Labelers

1. Assign yourself to this issue.
2. Go to the pull request that will be linked in a comment below (created by GitHub Actions).
3. Check out the branch locally:
   ```
   git fetch origin
   git checkout labeling-task-[Video-Name]-Batch-[Number]
   ```
4. Pull only the frames for your assigned batch:
   ```
   git lfs pull -I "[Video Name]/batch_[Number]/frames/*"
   ```
5. Label the images using Labelfficient:
   ```
   cd labelfficient
   python gui.py
   ```
   Set the "Dataset:" field to the absolute path of your frames folder, e.g.:
   ```
   C:\Users\username\baboon-hand-labeling\[Video Name]\batch_[Number]\frames
   ```
6. After completing the batch, commit your changes:
   ```
   git add "[Video Name]/batch_[Number]/frames_Annotations"
   git commit -m "Labeled [Video Name] batch [Number]"
   git push
   ```
7. Go back to the pull request on GitHub:
   - Leave a comment saying you've completed the task
   - A maintainer will review your work and merge the pull request if everything looks good
8. Close this issue when your labeling task is complete and the pull request has been merged.

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
- While labeling, it's helpful to open the images in your operating system's gallery application (like Windows "Photos") and flip through them. This allows you to see the full resolution images, as the labeling software compresses them for display.
- Instead of trying to label all baboons on a single frame before moving to the next, it may be easier to focus on one baboon and label it across all frames, then move on to the next baboon. This approach can help you track individual baboons more consistently.

## Checklist

- [ ] Assigned myself to this issue
- [ ] Checked out the correct branch
- [ ] Pulled the correct frames using Git LFS
- [ ] Labeled all relevant subjects in the batch
- [ ] Committed and pushed changes
- [ ] Commented on the pull request
- [ ] Closed this issue (after pull request is merged)