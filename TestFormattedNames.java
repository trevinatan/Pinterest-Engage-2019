import java.util.Arrays;
import java.util.List;

public class TestFormattedNames {

    public static void main (String[] args) {
        testFormatNames();
        testFormatNames2();
    }

    public static void testFormatNames() {
        FormattedNames fs = new FormattedNames();

        System.out.println(fs.formatNames(null));

        List<String> list1 = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println(fs.formatNames(list1));
    }

    public static void testFormatNames2() {
        FormattedNames fs = new FormattedNames();

        System.out.println(fs.formatNames2(null, 0));

        List<String> lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println(fs.formatNames2(lst, 2));
    }

}
