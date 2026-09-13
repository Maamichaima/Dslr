import sys
 
from data.loader import DataLoader
from data.preprocessing import Preprocessing

from statistics.correlation import find_most_correlated_pair
 

 
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py <dataset.csv>")
 
    path = sys.argv[1]
 
    loader = DataLoader(path)
    df = loader.load()
    prep = Preprocessing(df)

    print(find_most_correlated_pair(df, prep.numeric_cols))

    # print(prep.split_by_house("Defense Against the Dark Arts"))
    # incepect_data = prep.inspect_data("Astronomy")
    # print(incepect_data)
 
 
if __name__ == "__main__":
    main()

# Arithmancy