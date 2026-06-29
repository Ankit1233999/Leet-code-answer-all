class Solution:
    def dfs(self, city, isConnected, visited):
        visited[city] = True

        for neighbor in range(len(isConnected)):
            if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                self.dfs(neighbor, isConnected, visited)

    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces += 1
                self.dfs(city, isConnected, visited)

        return provinces