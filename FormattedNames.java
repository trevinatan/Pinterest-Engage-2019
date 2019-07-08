import java.util.List;

public class FormattedNames {
/**
 * LEVEL 1
 *
 * The exercise here is to write a function that takes a single argument (a
 * list of names) and returns a string representing the English-formatted
 * conjunction of those names.
 *
 * For example, given these names: ['Alice', 'Bob', 'Carlos', 'Diana']
 * The output would be: "Alice, Bob, Carlos and Diana"
 *
 * This type of function is useful when building user interfaces that show the
   list of people in a conversation, for example.
 *
 * Whether or not the output follows the Oxford comma rule is up to the author.
 **/

public static String formatNames(List<String> lst) {
    if (lst == null) {
        return null;
    }

    String res = "";
    int len = lst.size();
    for (int i = 0; i < len - 1; i++) {
        res += lst.get(i);
        res += ", ";
    }
    res += "and " + lst.get(len - 1);
    return res;
}

/**
 *  LEVEL 2
 *
 *  We iterate on the problem by adding a second argument to our function.
 *
 *  Now lets add a new argument called `limit`. This controls the maximum number of
 *  names that should be displayed. Any remaining items are "summarized" using the
 *  string "and # more".
 *
 *  For example, given these names: ['Alice', 'Bob', 'Carlos', 'Diana'] and limit: 2
 *
 *  The output would be: "Alice, Bob and 2 more"
 */

public static String formatNames2(List<String> lst, int limit) {
    if (lst == null) {
        return null;
    }
    int size = lst.size();
    String res = "";
    if (size < limit) {
        return formatNames(lst);
    }
    for (int i = 0; i < limit; i++) {
        res += lst.get(i);
        res += ", ";
    }
    res += "and " + (size - limit) + " more";
    return res;
}

/**
 *  LEVEL 3
 *
 *  Finally, write a function which prints the maximum
 *  possible number of names within the `max_chars` limit
 *  (versus the first N names that fit within the limit).
 */

}