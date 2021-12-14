def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        values = [1000,500,100,50,10,5,1]
        subtractions = [900,400,90,40,9,4,1]
        symbolForSubtractions = ["CM","CD","XC","XL","IX","IV"]
        symbols = ['M','D','C','L','X','V','I']
        retString = ""
        while num != 0:
            for i in range(len(values)):
                if num >= subtractions[i] and num < values[i]:
                    retString += symbolForSubtractions[i]
                    num -= subtractions[i]
                    break
                if num >= values[i]:
                    retString += symbols[i]
                    num -= values[i]
                    break
        return retString