"""
The test asks for finding first indexes of appearances
of a substring in a parent string. If there are no occurrences
of the substring in the parent string "<no matches>" will be
returned instead

---------------------------------------------------------------

There are various ways of searching for a substring in a string.
The naive way will include using a 'sliding window', of size
equal to the size of the substring, to iterate over the parent
string and compare characters at each step. This has time
complexity O(m*n).

---------------------------------------------------------------

Using KMP (Knuth-Morris-Prath) algorithm we can achieve a better
time complexity, namely O(n).

"""

# Toggle testing on/off:
testing = False

class StringMatch:
    """
    StringMatch uses KMP to perform substring search
    and aggregates the output indexes and then returns
    them.
    """
    @staticmethod
    def __computeLPP(subtext):
        """
        Method for computing the longest proper prefix array
        that will be used by the KMP algorithm.
        """
        m = len(subtext)
        lpp = [0] * m

        i = 1
        j = 0
        while i < m:
            if subtext[i] == subtext[j]:
                lpp[i] = j + 1
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lpp[j - 1]
                else:
                    lpp[i] = 0
                    i += 1
        return lpp

    @staticmethod
    def KMP(text, subtext):
        """
        Method performing the KMP algorithm on the input
        and storing the indexes of occurrences of substring.

        Returns a list with the occurrences indexes 
        -- <no matches> if there is no match.
        """
        if len(text) < len(subtext):
            return "<no matches>"

        if len(text) == len(subtext) and len(text) == 0:
            return [0]

        text = text.lower()
        subtext = subtext.lower()
        output = []

        lpp = StringMatch.__computeLPP(subtext)

        i = 0
        j = 0
        while i < len(text):
            if text[i] == subtext[j]:
                i += 1
                j += 1
            else:
                if j != 0:
                    j = lpp[j - 1]
                else:
                    i += 1
            if j == len(subtext):
                output.append(i - j)
                j = lpp[j - 1]

        return ([index + 1 for index in output], "<no matches>")[len(output) == 0]


if testing == False:
    # Reading input from console
    print("Input text:")
    text = input()
    print("Input subtext:")
    subtext = input()

    print(StringMatch.KMP(text, subtext))