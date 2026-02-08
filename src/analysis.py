"""
Name: Carla Fabiana Lorena Martinez Becerra
Date: 11/26/2025
Term: FA25
Course: ES1093

Final Project

Data Analysis
"""


import pandas as pd 
import matplotlib.pyplot as plt


# Analysis of average daily water consumption by borough over time
def main():
    df = pd.read_csv("NYCWater.csv", engine="python")
    
    df["Revenue Month"] = pd.to_datetime(df["Revenue Month"], format = "%Y-%m") # converting revenue month text into datetime year month

    df = df[df["Current Charges"] >= 0] # keeping rows where the current charges are not negative
    df = df.dropna(subset=["Consumption (HCF)", "# days"]) # dropping rows with missing consumption or days

    df = df[(df["# days"] > 0) & (df["# days"] < 366)] # filtering for realistic billing periods

    df["consumptionPerDay"] = df["Consumption (HCF)"] / df["# days"] # dividing consumption by the number of days


    # Computing the 95th percentile of consumption per day
    dailyThreshold = df["consumptionPerDay"].quantile(0.95) # determining a cut off for extreme daily usage
    # and filtering out the top 5 percent of daily consumption values to reduce the influence of outliers
    df = df[df["consumptionPerDay"] <= dailyThreshold] # keeping rows below or equal to the threshold


    groupedFrame = df.groupby(["Borough", "Revenue Month"])["consumptionPerDay"].mean().reset_index() # calculating mean per borough per month

    groupedFrame = groupedFrame.sort_values(by="Revenue Month") # sorting the data by month

    # Creating the ticks for the x axis to show only years and not each revenue month
    years = sorted(groupedFrame["Revenue Month"].dt.year.unique()) # collecting the unique years in order
    yearTickPositions = [] # empty list for tick positions
    yearTickLabels = [] # empty list for tick labels
    
    for year in years: # iterating over each year
        firstDateThisYear = groupedFrame[groupedFrame["Revenue Month"].dt.year == year]["Revenue Month"].min() # finding the first month of this year
        yearTickPositions.append(firstDateThisYear) # adding the first date of the year as a tick position
        yearTickLabels.append(str(year)) # adding the year as a string
    

    uniqueBoroughs = groupedFrame["Borough"].unique() # list of unique borough names

    # Creating a line plot for each borough
    plt.figure(figsize = (13, 6)) # making it wider and taller
    for borough in uniqueBoroughs: # iterating over each borough
        boroughData = groupedFrame[groupedFrame["Borough"] == borough] # filtering data for that specific borough
        boroughData = boroughData.sort_values(by="Revenue Month") # sorting data by month for plotting
        plt.plot(boroughData["Revenue Month"], boroughData["consumptionPerDay"], label=borough) # plotting mean daily consumption


    # Plottiiiiiing
    plt.title("Average Daily Water Consumption by Borough Over Time", fontsize = 14)
    plt.xlabel("Years of Service (Aggregated Revenue Months)", fontsize = 12)
    plt.ylabel("Average Consumption per Day (HCF)", fontsize = 12)
    plt.xticks(yearTickPositions, yearTickLabels, rotation = 90, fontsize = 8) # setting one tick per year at the first month of that year
    plt.legend()
    plt.tight_layout(rect = [0, 0, 0.8, 1])
    plt.legend(loc = "center left", bbox_to_anchor =(1, 0.5)) # placing the legend outside the main plot area on the right side
    plt.savefig("average_daily_consumption_borough.png")


    boroughMeans = df.groupby("Borough")["consumptionPerDay"].mean() # calculating mean daily consumption per borough
    
    print("Average daily consumption per borough:") # printing header for the borough means
    
    for boroughName, meanValue in boroughMeans.items(): # iterating through the means
        print(boroughName, ":", meanValue) # printing the borough and its average consumption


if __name__ == "__main__":
    main() # call the main function
