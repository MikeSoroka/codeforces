for _ in range(int(input())):
    n, m = map(int, input().split())
    adj = {i: [] for i in range(n)}
    for _ in range(m):
        start, end, color = map(int, input().split())
        adj[start - 1].append((end - 1, color))
        adj[end - 1].append((start - 1, color))


    dfs()

    visited = set()
    for i in range(n):
        if i in visited:
            continue

        visited.add(i)
        component = set()
        stack = [i]
        while stack:
            curr = stack.pop()
            if curr in component:
                continue

            component.add(curr)
            for neig in adj[curr]:
                stack.append(neig[0])

        can_ach = {}
        stack
