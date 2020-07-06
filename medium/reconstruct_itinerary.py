class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 0:
            return []

        next_cities = {}  # Dict of city to list of destination cities of that city
        for t in tickets:
            if t[0] not in next_cities.keys():
                next_cities[t[0]] = [t[1]]
            else:
                next_cities[t[0]].append(t[1])

        # Build path with smallest lexical order with greedy
        path = ["JFK"]
        curr = "JFK"
        while next_cities and curr in next_cities.keys():
            min_ = next_cities[curr][0]
            for c in next_cities[curr]:
                if c < min_:
                    min_ = c
            path.append(min_)
            next_cities[curr].remove(min_)
            if len(next_cities[curr]) == 0:
                del next_cities[curr]
            curr = min_
                
        if not next_cities:
            return path
        
        # If not all tickets are used, backtrack 
        # If a city is included in one of the unused tickets, then there must be 
        # a cycle back to that city, because other than the start and end node, all
        # nodes must have an even number of edges
        idx = -2
        while next_cities:
            while next_cities:
                curr = path[idx]
                if curr in next_cities.keys():
                    # Build path from curr
                    cycle = []
                    cycle_curr = curr
                    while cycle_curr != curr or len(cycle) == 0:
                        min_ = next_cities[cycle_curr][0]
                        for c in next_cities[cycle_curr]:
                            if c < min_:
                                min_ = c
                        cycle.append(min_)
                        next_cities[cycle_curr].remove(min_)
                        if len(next_cities[cycle_curr]) == 0:
                            del next_cities[cycle_curr]
                        cycle_curr = min_
                        
                    # Add list to after curr, because curr should be less than cycle
                    path = path[:idx+1] + cycle + path[idx+1:]
                    break                    
                idx -= 1
        return path
