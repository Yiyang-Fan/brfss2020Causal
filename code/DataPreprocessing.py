# This program preprocess the brfss data set.
# It cast SLEPTIM1 to categorical variable by a function catSleep
# It minus all categories by 1 to set the baseline as 0
# It fills missing value by -1
# It selects 33 columns from brfss2020.csv to form brfss2020Narrowed.csv
# It select 14 columns from brfss2020Narrowed.csv to form brfss2020Simple.csv
import pandas as pd
import dowhy

data = pd.read_csv("brfss2020.csv")

all_narrow_data = data[[
    "_SMOKER3",
    "_RFBING5",
    "SLEPTIM1",
    "_TOTINDA",
    "_BMI5CAT",
    "_RFHLTH",
    "_PHYS14D",
    "_MENT14D",
    "_HCVU651",
    "_MICHD",
    "_ASTHMS1",
    "_DRDXAR2",
    "_AIDTST4",
    "CVDINFR4",
    "CVDCRHD4",
    "CVDSTRK3",
    "DIABETE4",
    "CIMEMLOS",
    "_CHLDCNT",
    "_INCOMG",
    "MARITAL",
    "RENTHOM1",
    "EMPLOY1",
    "_RACEPRV",
    "_AGE_G",
    "_EDUCAG",
    "_URBSTAT",
    "_SEX",
    "SOFEMALE",
    "TRNSGNDR",
    "ACEDRINK",
    "ACEDIVRC",
    "VETERAN3"
]]
def catSleep(x):
    if x < 4:
        return 1
    elif x < 7:
        return 2
    elif x < 10:
        return 3
    else:
        return 4
all_narrow_data["SLEPTIM1"] = all_narrow_data["SLEPTIM1"].apply(lambda x: catSleep(x))

all_narrow_data = all_narrow_data - 1
all_narrow_data = all_narrow_data.fillna(-1)

all_narrow_data.to_csv("brfss2020Narrowed.csv")

print(all_narrow_data.nunique().values)
print(all_narrow_data.describe())

treatment = ["_SMOKER3", "_RFBING5", "SLEPTIM1", "_TOTINDA"]
outcome = ["_RFHLTH", "_PHYS14D", "_MENT14D"]
confounder = ["_INCOMG", "MARITAL", "_EDUCAG", "_URBSTAT", "_RACEPRV", "_AGE_G", "_SEX"]
illness = ["_HCVU651", "_MICHD", "_ASTHMS1", "_DRDXAR2", "_AIDTST4", "CVDINFR4", "CVDCRHD4", "CVDSTRK3", "DIABETE4", "CIMEMLOS"]

simple_data = all_narrow_data[treatment + outcome + confounder]

simple_data.to_csv("brfss2020Simple.csv")
