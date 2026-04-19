from __future__ import annotations


class AOStarGraph:
    def __init__(self, graph: dict[str, list[list[tuple[str, int]]]], heuristic: dict[str, int], start: str):
        self.graph = graph
        self.heuristic = heuristic.copy()
        self.start = start
        self.parent: dict[str, str] = {}
        self.status: dict[str, int] = {}
        self.solution_graph: dict[str, list[str]] = {}

    def neighbors(self, node: str) -> list[list[tuple[str, int]]]:
        return self.graph.get(node, [])

    def min_cost_children(self, node: str) -> tuple[int, list[str]]:
        options = self.neighbors(node)
        if not options:
            return 0, []

        best_cost = float("inf")
        best_children: list[str] = []
        for child_group in options:
            cost = sum(weight + self.heuristic[child] for child, weight in child_group)
            children = [child for child, _ in child_group]
            if cost < best_cost:
                best_cost = cost
                best_children = children
        return int(best_cost), best_children

    def solve(self, node: str | None = None, backtracking: bool = False) -> None:
        current = node or self.start
        if self.status.get(current) == -1:
            return

        best_cost, best_children = self.min_cost_children(current)
        self.heuristic[current] = best_cost
        self.status[current] = len(best_children)

        solved = True
        for child in best_children:
            self.parent[child] = current
            if self.status.get(child) != -1:
                solved = False

        if solved:
            self.status[current] = -1
            self.solution_graph[current] = best_children
            if current != self.start:
                self.solve(self.parent[current], backtracking=True)
            return

        if not backtracking:
            for child in best_children:
                if self.status.get(child) != -1:
                    self.solve(child, backtracking=False)

            best_cost, best_children = self.min_cost_children(current)
            self.heuristic[current] = best_cost
            if all(self.status.get(child) == -1 for child in best_children):
                self.status[current] = -1
                self.solution_graph[current] = best_children
                if current != self.start:
                    self.solve(self.parent[current], backtracking=True)

    def run(self) -> dict[str, list[str]]:
        self.solve(self.start)
        return self.solution_graph


def main() -> None:
    heuristic_one = {"A": 1, "B": 6, "C": 2, "D": 12, "E": 2, "F": 1, "G": 5, "H": 7, "I": 7, "J": 1, "T": 3}
    graph_one = {
        "A": [[("B", 1), ("C", 1)], [("D", 1)]],
        "B": [[("G", 1)], [("H", 1)]],
        "C": [[("J", 1)]],
        "D": [[("E", 1), ("F", 1)]],
        "G": [[("I", 1)]],
    }

    heuristic_two = {"A": 1, "B": 6, "C": 12, "D": 10, "E": 4, "F": 4, "G": 5, "H": 7}
    graph_two = {
        "A": [[("B", 1), ("C", 1)], [("D", 1)]],
        "B": [[("G", 1)], [("H", 1)]],
        "D": [[("E", 1), ("F", 1)]],
    }

    solution_one = AOStarGraph(graph_one, heuristic_one, "A").run()
    solution_two = AOStarGraph(graph_two, heuristic_two, "A").run()

    print("Experiment 2(b): AO* Search")
    print(f"Solution graph 1: {solution_one}")
    print(f"Solution graph 2: {solution_two}")


if __name__ == "__main__":
    main()
