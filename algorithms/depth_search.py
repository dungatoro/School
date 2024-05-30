def dfs(graph):
	current = next(iter(graph))
	visited = {key: False for key in graph}
	stack = [current]
	visited[current] = True
	print(f"Starting in {current}.")
	while len(stack) > 0:
		unvisited = [n for n in graph[current] if not visited[n]]	
		if len(unvisited) == 0:
			current = stack.pop()
			if len(stack) == 0: print(f"Finished!")
			else: print(f"Backtracking to {current}.")
		else:
			stack.append(current)
			current = unvisited[0]
			visited[current] = True
			print(f"Moved on to {current}.")
