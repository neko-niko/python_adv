def make_averager():
    series = []
    def averager(value):
        series.append(value)
        total = sum(series)
        return total / len(series)
    return averager
