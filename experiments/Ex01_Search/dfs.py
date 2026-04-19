GRAPH = {
    "A": ["B", "S"],
    "B": ["A"],
    "S": ["A", "C", "G"],
    "C": ["S", "D", "E", "F"],
    "D": ["C"],
    "E": ["C", "H"],
    "F": ["C", "G"],
    "G": ["S", "F", "H"],
    "H": ["E", "G"],
}


def dfs(graph: dict[str, list[str]], start: str, goal: str) -> tuple[list[str], list[str]]:
    stack = [start]
    parents = {start: None}
    visited = set()
    expansion_order: list[str] = []

    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        expansion_order.append(current)
        if current == goal:
            break
        for neighbor in reversed(graph[current]):
            if neighbor not in visited and neighbor not in parents:
                parents[neighbor] = current
            if neighbor not in visited:
                stack.append(neighbor)

    path: list[str] = []
    node = goal
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path, expansion_order


def main() -> None:
    start, goal = "A", "H"
    path, expansion_order = dfs(GRAPH, start, goal)

    print("Experiment 1(b): Depth First Search")
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print(f"Expansion order: {' -> '.join(expansion_order)}")
    print(f"Path: {' => '.join(path)}")
    print(f"Path length: {len(path) - 1}")


if __name__ == "__main__":
    main()
