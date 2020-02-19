class StringMatch:

    @staticmethod
    def __computeLPP(subtext):
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
        
        text = text.lower()
        subtext = subtext.lower()

        lpp = StringMatch.__computeLPP(subtext)

        output = []

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


text = input()
subtext = input()

print(StringMatch.KMP(text, subtext))