import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TestFormattedNames {

    public static void main (String[] args) {
        //testFormatNames();
        //testFormatNames2();
        testFormatNames3();
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
        System.out.println(fs.formatNames2(lst, 0));
    }

    public static void testFormatNames3() {
        FormattedNames fs = new FormattedNames();

        System.out.println(fs.formatNames3(null, 0));
        List<String> lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println("Expected: and 4 more");
        System.out.print("Actual: ");
        System.out.println(fs.formatNames3(lst, 0));
        System.out.println();


        lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println("Expected: Alice, Bob, and 2 more");
        System.out.print("Actual: ");
        System.out.println(fs.formatNames3(lst, 8));
        System.out.println();


        lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println("Expected: Alice, Bob, Carlos, and 1 more");
        System.out.print("Actual: ");
        System.out.println(fs.formatNames3(lst, 14));
        System.out.println();


        lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println("Expected: Alice, Bob, Carlos, and 1 more");
        System.out.print("Actual: ");
        System.out.println(fs.formatNames3(lst, 16));
        System.out.println();

        lst = Arrays.asList("Alice", "Bob", "Carlos", "Diana");
        System.out.println("Expected: Alice, Bob, Carlos, and Diana");
        System.out.print("Actual: ");
        System.out.println(fs.formatNames3(lst, 30));
        System.out.println();


    }

}
