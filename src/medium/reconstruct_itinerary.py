from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """This is very similiar to the bridge problem, since it is possible to traverse this, the             start node is either a node with odd edges or it is in a loop"""
        if len(tickets) == 0:
            return []

        # Find start node by finding node with odd edges
        next_cities = {}  # Dict of city to list of destination cities of that city
        edge_count = {}  # Dict of city to edge count included edges into city
        for t in tickets:
            if t[0] not in next_cities.keys():
                next_cities[t[0]] = [t[1]]
            else:
                next_cities[t[0]].append(t[1])

            if t[0] not in edge_count.keys():
                edge_count[t[0]] = 1
            else:
                edge_count[t[0]] += 1

            if t[1] not in edge_count.keys():
                edge_count[t[1]] = 1
            else:
                edge_count[t[1]] += 1

        odd_cities = []
        for c in edge_count.keys():
            if edge_count[c] % 2 == 1:
                odd_cities.append(c)

        if len(odd_cities) == 2:
            start = odd_cities[0] if odd_cities[0] < odd_cities[1] else odd_cities[1]
        elif len(odd_cities) == 0:
            start = tickets[0][0]
            for c in next_cities.keys():
                if c < start:
                    start = c
        else:
            return ["LOL"]

        # Build path with smallest lexical order with greedy
        path = [start]
        curr = start
        while len(next_cities.keys()) > 0:
            next_ = next_cities[curr][0]
            for o in next_cities[curr]:
                if o < next_:
                    next_ = o
            next_cities[curr].remove(next_)
            if len(next_cities[curr]) == 0:
                del next_cities[curr]
            path.append(next_)
            curr = next_

        return path


if __name__ == "__main__":
    f = Solution().findItinerary
    print(f([["JFK", "ATL"], ["ATL", "JFK"]]))
