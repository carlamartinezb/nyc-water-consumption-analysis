"""
Name: Carla Fabiana Lorena Martinez Becerra
Date: 11/26/2025
Term: FA25
Course: ES1093

Final Project

Data Exploration
"""


import pandas as pd 
import matplotlib.pyplot as plt


def main():
    
    waterData = pd.read_csv("NYCWater.csv", engine="python")


    #print("HEADERS:")
    #print(waterData.head)

    #print("\nCOLUMN NAMES:")
    #print(waterData.columns)

    #print("\nSHAPE (ROWS, COLUMNS):")
    #print(waterData.shape)

    #print("\nDATA TYPES:")
    #print(waterData.dtypes)

    #print("\nNUMERIC SUMMARY:")
    #print(waterData.describe())

    #print("\nLAST FIVE ROWS:")
    #print(waterData.tail())
    

    """
    # Plot 1: Histogram of consumption
    plt.figure()
    plt.hist(waterData["Consumption (HCF)"])
    plt.title("Histogram of Consumption (HCF)")
    plt.xlabel("Consumption (HCF)")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("consumption_histogram.png")

    # Plot 2: Histogram of charges
    plt.figure()
    plt.hist(waterData["Current Charges"])
    plt.title("Histogram of Current Charges")
    plt.xlabel("Current Charges ($)")
    plt.ylabel("Number of Records")
    plt.tight_layout()
    plt.savefig("currentcharges_histogram.png")"""

    # After doing the plots, I was curious to know some details of those fields

    #print("Consumption (HCF)")
    #print("max:", waterData["Consumption (HCF)"].max())
    #print("min:", waterData["Consumption (HCF)"].min())
    #print("mean:", waterData["Consumption (HCF)"].mean())
    #print("median:", waterData["Consumption (HCF)"].median())

    #print("\nCurrent Charges")
    #print("max:", waterData["Current Charges"].max())
    #print("min:", waterData["Current Charges"].min())
    #print("mean:", waterData["Current Charges"].mean())
    #print("median:", waterData["Current Charges"].median())

    # Examining anomalies:

    # counting negative and zero charges
    negativeChargesCount = (waterData["Current Charges"] < 0).sum() # number of negative charges
    zeroChargesCount = (waterData["Current Charges"] == 0).sum() # number of zero charges

    # counting zero and missing consumption
    zeroConsumptionCount = (waterData["Consumption (HCF)"] == 0).sum() # zero consumption
    missingConsumptionCount = waterData["Consumption (HCF)"].isna().sum() # NaN consumption

    #print("negative charges:", negativeChargesCount)
    #print("zero charges:", zeroChargesCount)
    #print("zero consumption:", zeroConsumptionCount)
    #print("missing consumption:", missingConsumptionCount)

    # removing negative charges and missing consumption
    cleanedFrame = waterData[waterData["Current Charges"] >= 0].copy()
    cleanedFrame = cleanedFrame.dropna(subset=["Consumption (HCF)"])

    # computing 95th percentiles
    consumption95 = cleanedFrame["Consumption (HCF)"].quantile(0.95)
    charges95 = cleanedFrame["Current Charges"].quantile(0.95)

    # filtering out the values above the 95th percentile
    filteredFrame = cleanedFrame[(cleanedFrame["Consumption (HCF)"] <= consumption95) & (cleanedFrame["Current Charges"] <= charges95)]

    #print(filteredFrame)

    print("the new frame stats")
    print("\nConsumption (HCF)")
    print("max:", filteredFrame["Consumption (HCF)"].max())
    print("min:", filteredFrame["Consumption (HCF)"].min())
    print("mean:", filteredFrame["Consumption (HCF)"].mean())
    print("median:", filteredFrame["Consumption (HCF)"].median())

    print("\nCurrent Charges")
    print("max:", filteredFrame["Current Charges"].max())
    print("min:", filteredFrame["Current Charges"].min())
    print("mean:", filteredFrame["Current Charges"].mean())
    print("median:", filteredFrame["Current Charges"].median())


if __name__ == "__main__":
    main()
