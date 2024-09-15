import pandas as pd  # imports pandas and calls the imported version 'pd'
import matplotlib.pyplot as plt  # imports the package and calls it 'plt'

from main import get_statistics, build_barplot

def test_statistics():
    result1 = get_statistics()
    assert result1 is not None

def test_plot():
    result2 = build_barplot()
    assert result2 is not None

if __name__=="__main__":
    test_statistics()
    test_plot()