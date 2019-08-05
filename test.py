import unittest
import NumberTranslator

class TestSum(unittest.TestCase):

    def test_zeroNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(0), 'zero')

    def test_unitNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(1), 'one')

    def test_teenNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(10), 'ten')

    def test_teenNumberToText2(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(15), 'fifteen')

    def test_tensNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(67), 'sixty seven')

    def test_hundredsNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(811), 'eight hundred eleven')

    def test_containingzeroNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(10000), 'ten thousand')

    def test_containingzeroNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(10000101), 'ten million one hundred one')

    def test_floatNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(14.03665), 'fourteen point zero three six six five')

    def test_bigNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(231111101111.11), 'two hundred thirty one trillion one hundred eleven billion one hundred one million one hundred eleven thousand one hundred eleven point one one')

    def test_negativeNumberToText(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(-386), 'minus three hundred eighty six')

    def test_zeroTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('zero'), 0)

    def test_smallTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('three'), 3)

    def test_mediumTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('ten'), 10)

    def test_mediumTextToNumber2(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('fourteen'), 14)

    def test_mediumTextToNumber3(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('fifty one'), 51)

    def test_mediumTextToNumber4(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('three hundred fifty one'), 351)

    def test_bigTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('ten million six hundred fifty one'), 10000651)

    def test_floatTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('ten point five'), 10.5)

    def test_floatTextToNumber2(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('nine point five three one'), 9.531)

    def test_minusTextToNumber(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('minus four point two'), -4.2)

    #test from email

    def test_01(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(111), 'one hundred eleven')

    def test_02(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(4032), 'four thousand thirty two')

    def test_03(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(87413), 'eighty seven thousand four hundred thirteen')

    def test_04(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate(45.2), 'forty five point two')

    def test_05(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('Ten Thousand Four Hundred Eighty Two'), 10482)

    def test_06(self):
        translator = NumberTranslator.Translator()
        self.assertEqual(translator.translate('Zero point Nine'), 0.9)

if __name__ == '__main__':
    unittest.main()
