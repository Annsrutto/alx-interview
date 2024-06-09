def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened"""
    if not boxes:
        return False

    n = len(boxes)
    unlocked = set([0])
    queue = [0]

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == n
