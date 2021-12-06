from statistics import mean, median
from numpy import polyfit, poly1d


class Party:
    def __init__(self, data, party):
        self.xAxis = []
        self.yAxis = []
        try:
            for item in data:
                if item[3] == party:
                    self.xAxis.append(int(item[2]))
                    self.yAxis.append(int(item[1]))
        except SyntaxError:
            print(f"No items matching '{party}' in list")
        if len(self.xAxis) != 0 and len(self.yAxis) != 0:
            self.xAverage = mean(self.xAxis)
            self.yAverage = mean(self.yAxis)
            self.xMedian = median(self.xAxis)
            self.yMedian = median(self.yAxis)

    def trend_line(self):
        z = polyfit(self.xAxis, self.yAxis, 1)
        p = poly1d(z)
        return p(self.xAxis)
