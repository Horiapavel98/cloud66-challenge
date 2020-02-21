import substring_matcher
import unittest

class StringMatchTest(unittest.TestCase):
    def testGivenInputsFromRequirementsPaper(self):
        text = "Polly put the kettle on, polly put the kettle on, polly put the kettle on we'll all have tea"
        subtext1 = "Polly" ; expected1 = [1, 26, 51]
        subtext2 = "polly" ; expected2 = [1, 26, 51]
        subtext3 = "ll"    ; expected3 = [3, 28, 53, 78, 82]
        subtext4 = "Ll"    ; expected4 = [3, 28, 53, 78, 82]
        subtext5 = "X"     ; expected5 = "<no matches>"
        subtext6 = "Polx"  ; expected6 = "<no matches>"

        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext1), expected1)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext2), expected2)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext3), expected3)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext4), expected4)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext5), expected5)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext6), expected6)

    def testForCustomInput(self):
        text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
        Donec tellus ligula, volutpat eget dui in, accumsan lobortis metus. 
        Suspendisse vitae orci purus. Sed vestibulum magna in eros tempus 
        hendrerit. Ut id pharetra magna. Vivamus tempor metus sit amet nisi 
        aliquet, aliquet auctor purus iaculis. Suspendisse aliquet accumsan 
        maximus. Integer nec iaculis libero. Suspendisse in eleifend felis. 
        Morbi vel diam sed orci tincidunt placerat. Etiam faucibus condimentum 
        nisl, at placerat odio feugiat vitae. Vestibulum gravida eget nisi vel 
        malesuada. In vestibulum nunc vel lectus sagittis, non blandit mauris 
        tristique. Nulla facilisi. Pellentesque eu tortor elementum, maximus 
        purus ac, viverra dolor. Maecenas."""

        subtext1 = "abda"               ; expected1 = "<no matches>"
        subtext2 = "ae"                 ; expected2 = [159, 564, 793]
        subtext3 = "ll"                 ; expected3 = [75, 702, 718]
        subtext4 = "nulla faciliSI"     ; expected4 = [700]
        subtext5 = "X"                  ; expected5 = [375, 752]
        subtext6 = "vEsTi"              ; expected6 = [178, 568, 624]

        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext1), expected1)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext2), expected2)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext3), expected3)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext4), expected4)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext5), expected5)
        self.assertEqual(substring_matcher.StringMatch.KMP(text, subtext6), expected6)

    def testForBoundaries(self):
        # Test boundaries here