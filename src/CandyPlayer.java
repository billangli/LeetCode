import java.util.Random;
import java.util.Scanner;

public class CandyPlayer {

    private static int totalCandy = (new Random()).nextInt(100);
    private static int turn = 0;
    private static int numPlayers = 0;
    private int id;
    private int numCandy;

    public CandyPlayer(int num) {
        this.numCandy = num;
        this.id = numPlayers;
        numPlayers += 1;
    }

    public int getMyCandy(){
        return this.numCandy;
    }

    public static int getMountainCandy() {
        return totalCandy;
    }

    public static int getTurn() {
        return turn;
    }

    public static int getNumberOfPlayers() {
        return numPlayers;
    }

    public static void setTurn(int turn) {
        CandyPlayer.turn = turn;
    }

    public static void setNumberOfPlayers(int num) {
        CandyPlayer.numPlayers = num;
    }

    public boolean play(int num) {
        if ((num > this.numCandy) || (this.id != CandyPlayer.turn)) {
            return false;
        } else {
            if (totalCandy >= 2 * num) {
                totalCandy += num;
                this.numCandy -= num;
                this.numCandy += 2 * num;
                totalCandy -= 2 * num;
            } else {
                totalCandy += num;
                this.numCandy -= num;
            }
            CandyPlayer.turn++;
            if (CandyPlayer.numPlayers == CandyPlayer.turn) {
                CandyPlayer.turn = 0;
            }
            return true;
        }
    }

    public static void main(String[] args) {
        CandyPlayer p0 = new CandyPlayer(100);
        CandyPlayer p1 = new CandyPlayer(100);
        CandyPlayer p2 = new CandyPlayer(100);
        CandyPlayer p3 = new CandyPlayer(100);
        CandyPlayer[] cp = {p0, p1, p2, p3};
        Scanner input = new Scanner(System.in);

        while (CandyPlayer.getMountainCandy() > 0) {
            int turn = CandyPlayer.getTurn();
            System.out.println("---\nTurn " + turn);
            System.out.println("Player " + turn + " enter number of candy.");
            int num = input.nextInt();
            System.out.println(cp[turn].play(num));
            System.out.println("Player " + turn + " has " + cp[turn].getMyCandy() + " candies.");
            System.out.println("Candy Mountain has " + CandyPlayer.getMountainCandy() + " candies.");
        }
    }
}