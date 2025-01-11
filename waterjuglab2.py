
# Define the possible actions (state transitions)
def successors(state):
    X, Y = state
    succ = []

    # Action 1: Fill Jug X (capacity 4)
    if X < 4:
        succ.append((4, Y))

    # Action 2: Fill Jug Y (capacity 3)
    if Y < 3:
        succ.append((X, 3))

    # Action 3: Empty Jug X
    if X > 0:
        succ.append((0, Y))

    # Action 4: Empty Jug Y
    if Y > 0:
        succ.append((X, 0))

    # Action 5: Pour from Jug X to Jug Y
    if X > 0 and Y < 3:
        transfer = min(X, 3 - Y)
        succ.append((X - transfer, Y + transfer))

    # Action 6: Pour from Jug Y to Jug X
    if Y > 0 and X < 4:
        transfer = min(Y, 4 - X)
        succ.append((X + transfer, Y - transfer))

    return succ

# DFS algorithm
def dfs(initial_state, goal_state):
    OPEN = [initial_state]  # Stack of states to explore
    CLOSED = set()          # Set of explored states
    parent_map = {initial_state: None}  # To reconstruct the path

    while OPEN:
        # Step 1: Pop from OPEN and add it to CLOSED
        current_state = OPEN.pop()
        CLOSED.add(current_state)

        # Step 2: Goal test
        if current_state == goal_state:
            # Goal found, reconstruct path
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state = parent_map[current_state]
            return path[::-1]  # Return reversed path

        # Step 3: Generate successors and add to OPEN if not in OPEN or CLOSED
        for succ in successors(current_state):
            if succ not in CLOSED and succ not in OPEN:
                OPEN.append(succ)
                parent_map[succ] = current_state

    # Step 5: Return None if goal is not found
    return None

# Define the initial and goal states
initial_state = (0, 0)  # Initial state: both jugs empty
goal_state = (2, 0)     # Goal state: jug X has exactly 2 liters

# Run DFS to find the solution
solution = dfs(initial_state, goal_state)

# Output the solution
if solution:
    print("Solution path:")
    for step in solution:
        print(step)
else:
    print("No solution found")