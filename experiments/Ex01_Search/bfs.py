from collections import deque


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


def bfs(graph: dict[str, list[str]], start: str, goal: str) -> tuple[list[str], list[str]]:
    queue = deque([start])
    parents = {start: None}
    visited = {start}
    expansion_order: list[str] = []

    while queue:
        current = queue.popleft()
        expansion_order.append(current)
        if current == goal:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parents[neighbor] = current
                queue.append(neighbor)

    path: list[str] = []
    node = goal
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path, expansion_order


def main() -> None:
    start, goal = "A", "H"
    path, expansion_order = bfs(GRAPH, start, goal)

    print("Experiment 1(a): Breadth First Search")
    print(f"Start: {start}")
    print(f"Goal: {goal}")
    print(f"Expansion order: {' -> '.join(expansion_order)}")
    print(f"Path: {' => '.join(path)}")
    print(f"Path length: {len(path) - 1}")


if __name__ == "__main__":
    main()
