class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        alice_wins = {}
        def simulate(n: int, alice: bool) -> bool:
            if n == 0:
                return not alice
            if n in alice_wins.keys():
                return alice_wins[n] if alice else not alice_wins[n]
            if alice:
                for i in range(math.floor(math.sqrt(n)), 0, -1):
                    if simulate(n - i ** 2, not alice):
                        alice_wins[n] = True
                        return True
                alice_wins[n] = False
                return False
            else:
                for i in range(math.floor(math.sqrt(n)), 0, -1):
                    if not simulate(n - i ** 2, not alice):
                        alice_wins[n] = True
                        return False
                alice_wins[n] = False
                return True
                
        return simulate(n, True)
