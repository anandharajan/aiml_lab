GRAPH = {
    "A": [("B", 6), ("F", 3)],
    "B": [("C", 3), ("D", 2)],
    "C": [("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 8)],
    "E": [("I", 5), ("J", 5)],
    "F": [("G", 1), ("H", 7)],
    "G": [("I", 3)],
    "H": [("I", 2)],
    "I": [("E", 5), ("J", 3)],
    "J": [],
}

HEURISTIC = {
    "A": 10,
    "B": 8,
    "C": 5,
    "D": 7,
    "E": 3,
    "F": 6,
    "G": 5,
    "H": 3,
    "I": 1,
    "J": 0,
}


def a_star(start: str, goal: str) -> tuple[list[str], int]:
    open_set = {start}
    closed_set: set[str] = set()
    g_score = {start: 0}
    parents = {start: None}

    while open_set:
        current = min(open_set, key=lambda node: g_score[node] + HEURISTIC[node])
        if current == goal:
            break

        open_set.remove(current)
        closed_set.add(current)

        for neighbor, weight in GRAPH[current]:
            candidate_score = g_score[current] + weight
            if neighbor not in g_score or candidate_score < g_score[neighbor]:
                g_score[neighbor] = candidate_score
                parents[neighbor] = current
                if neighbor in closed_set:
                    closed_set.remove(neighbor)
                open_set.add(neighbor)

    path: list[str] = []
    node = goal
    while node is not None:
        path.append(node)
        node = parents[node]
    path.reverse()
    return path, g_score[goal]


def main() -> None:
    path, total_cost = a_star("A", "J")
    print("Experiment 2(a): A* Search")
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {total_cost}")


if __name__ == "__main__":
    main()
