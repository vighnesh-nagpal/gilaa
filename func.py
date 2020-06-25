import pandas as pd
def elemAbunIsReliable(df,elem=None):
    if elem==None:
        print("An element symbol must be provided")
    elif not isinstance(elem, str):
        print("The element name must be a string")
    elif not isinstance(df, pd.core.frame.DataFrame):
        print("Argument must be a pandas data frame")
    else:
        elemLower=elem.lower()
        if "flag_" + elemLower + "_fe" in df.columns:
            for i in range(len(df["flag_"+elemLower+"_fe"])):
                    if df["flag_"+elemLower+"_fe"][i] == 0:
                        print("Elemental abundance of " + elemLower + " is reliable for star " + df["star_id"][i])
                    else:
                        print("Elemental abundance of " + elemLower + " is not reliable for star " + df["star_id"][i])
        else:
            print("The elemental abundance for this element is not available")
        
teststars = pd.read_csv("testdata.csv")

df = pd.DataFrame(teststars)

elemAbunIsReliable(df,elem="eu")