import java.util.Arrays;
import java.util.Comparator;

public class SomeType {}

class GenericComparator implements Comparator<SomeType> {
    @Override
    public int compare(SomeType o1, SomeType o2) {
        return 0;
    }

    public static void main(String[] args) {
        SomeType[] array = {new SomeType(), new SomeType()};
        Arrays.sort(array, new GenericComparator());
    }
}