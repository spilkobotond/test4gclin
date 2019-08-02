import texts


class Translator:

    def __init__(self, number=0, text=''):
        self.number = number
        self.text = text

    def translate(self, input):
        if isinstance(input, int):
            return self.translateInteger(input)
        elif isinstance(input, float):
            return self.translateFloat(input)
        elif isinstance(input, str):
            return self.translateText(input)
        else:
            print('Bad input:')
            print(input.__class__)

    def translateFloat(self, number):
        frac = str(number).split('.')[1]
        self.translateInteger(int(number))
        self.text = self.text + ' point'
        for x in frac:
            self.text = self.text + ' ' + texts.units[int(x)]
        return self.text.strip()

    def translateInteger(self, number):
        if number < 0:
            self.text = 'minus'
            number = abs(number)
        numberString = str(number)
        numberLength = len(numberString)
        if numberLength < 2:
            self.text = self.text + ' ' + texts.units[int(numberString)]
        elif numberLength == 2:
            if number < 20:
                self.text = self.text + ' ' + texts.teens[number - 10]
            else:
                self.text = self.text + ' ' + texts.tens[int(numberString[0])]
                self.translate(int(numberString[1]))
        elif numberLength == 3:
            self.text = self.text + ' ' + texts.units[int(numberString[0])] + ' ' + texts.hundreds[0]
            self.translate(int(numberString[1:3]))
        elif numberLength > 3:
            numberOfBigParts = numberLength // 3
            lastDecimal = numberLength % 3
            if lastDecimal == 0:
                lastDecimal = 3
            i = 0
            # big part
            for x in range(numberOfBigParts, 0, -1):
                if i == 0:
                    subString = int(numberString[(0):(lastDecimal)])
                else:
                    subString = int(numberString[(lastDecimal + (i - 1) * 3):(lastDecimal + i * 3)])
                if subString != 0:
                    self.translate(subString)
                    self.text = self.text + ' ' + texts.hundreds[x]
                i = i + 1
            # below thousand part
            if int(numberString[-3:]) != 0:
                self.translate(int(numberString[-3:]))

        return self.text.strip()

    def translateText(self, text):
        lowerCaseText = text.lower()
        parts = lowerCaseText.split()
        negative = False
        if parts[0] == 'minus':
            negative = True
            del parts[0]
        decimal = 0
        tempNumber = 0
        for part in parts:
            if part in texts.units:
                if decimal < 0:
                    self.number = self.number + texts.units.index(part) * pow(10, decimal)
                    decimal = decimal - 1
                else:
                    tempNumber = tempNumber + texts.units.index(part)
            elif part in texts.teens:
                tempNumber = tempNumber + texts.teens.index(part) + 10
            elif part in texts.tens:
                tempNumber = tempNumber + texts.tens.index(part) * 10
            elif part in texts.hundreds:
                multiplier = 0
                ind = texts.hundreds.index(part)
                if ind == 0:
                    multiplier = 100
                elif ind == 1:
                    multiplier = 1000
                elif ind > 1:
                    multiplier = pow(10, 3 * (ind))
                self.number = self.number + tempNumber * multiplier
                tempNumber = 0
            elif part == 'point':
                decimal = -1
            else:
                print('Bad input: ' + part)
                break
        self.number = self.number + tempNumber
        if negative:
            self.number = self.number * (-1)
        return self.number
