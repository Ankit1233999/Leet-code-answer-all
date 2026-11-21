class Solution:
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the new parent of every node
        new_parent = parent[:]

        # Track nearest ancestor having each character
        last_seen = {}

        def dfs(node):
            ch = s[node]

            # Find the nearest ancestor with the same character
            if ch in last_seen:
                new_parent[node] = last_seen[ch]

            # Save previous value to restore after DFS
            old = last_seen.get(ch, -1)

            # Current node becomes the nearest node for this character
            last_seen[ch] = node

            # Visit children in the ORIGINAL tree
            for child in children[node]:
                dfs(child)

            # Restore path state
            if old == -1:
                del last_seen[ch]
            else:
                last_seen[ch] = old

        dfs(0)

        # Build the final tree using new parents
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

       # subtree sizes in the final tree
        answer = [0] * n

        def calculate_size(node):
            size = 1

            for child in new_children[node]:
                size += calculate_size(child)

            answer[node] = size
            return size

        calculate_size(0)

        return answer