def canUnlockAll(boxes):
  # Create a set to keep track of which boxes have been opened
  opened_boxes = set()
  # Add the first box to the set
  opened_boxes.add(0)
  # Create a queue for breadth-first search
  queue = [0]
  
  # Run breadth-first search
  while queue:
    box = queue.pop(0)
    for key in boxes[box]:
      if key not in opened_boxes:
        opened_boxes.add(key)
        queue.append(key)
  # Check if all boxes have been opened
  return len(opened_boxes) == len(boxes)
