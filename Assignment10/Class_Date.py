class Date:
    def __init__(self, d, m, y, t):
        # properties
        self.day = d
        self.month = m
        self.year = y
        self.TypeOfYear = t

    # methods
    def ConvertToSolarDate(self):
        ...
    
    def ConvertToLunarDate(self):
        ...

    def convertToDays(self):
        ...

    def convertToMonths(self):
        ...

    def CompareDates(self):
        ...

