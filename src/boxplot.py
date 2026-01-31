import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

def main():
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame

    plt.figure()
    df["MedHouseVal"].plot(kind="box")
    plt.title("California Housing: Median House Value")
    plt.ylabel("Median House Value ($100,000s)")

    plt.savefig("figs/boxplot.png", bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    main()