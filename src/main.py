import sys
 
from data.loader import DataLoader
from data.preprocessing import Preprocessing
 
 
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py <dataset.csv>")
 
    path = sys.argv[1]
 
    loader = DataLoader(path)
    df = loader.load()

    print(loader.identify_numeric_columns(df))
    print(df["Defense Against the Dark Arts"])

    # loader.display(df.head())
 
    # prep = Preprocessing(df)
    # incepect_data = prep.inspect_data("Astronomy")
    # print(incepect_data)
 
 
if __name__ == "__main__":
    main()