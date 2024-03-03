import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def outliers_det_salary(df):
    outliers = (df["salary"][(df["salary"] > (df["salary"].mean() + 3 * df["salary"].std()))]).index
    return outliers

def plots_salary_matplotlib(iterator, df):
    plt.figure(figsize = (10,10))
    plt.subplot(1, 2, 1)
    plt.hist(df["salary"])
    plt.title(iterator)
    plt.xlabel("Salary")

    plt.subplot(1, 2, 2)
    plt.violinplot(df["salary"])
    plt.xlabel("Salary")
    plt.show()

def conditioning_dataframe(df):
    cond = outliers_det_salary(df)
    i = 1
    while len(cond) != 0:
        df.drop(cond, inplace = True)
        df["salary_z_score"] = (df["salary"] - df["salary"].mean())/df["salary"].std()
        plots_salary_matplotlib(i, df)  
        print(f"Iteration {i}: \n", df["salary_z_score"].describe())
        i += 1
        cond = outliers_det_salary(df)

if __name__ == "__main__":
    print("Library for outilers detection and remotion")