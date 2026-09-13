import sys
 
from data.loader import DataLoader
from data.preprocessing import Preprocessing
 

 
def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py <dataset.csv>")
 
    path = sys.argv[1]
 
    loader = DataLoader(path)
    df = loader.load()
    # print(df["Arithmancy"].replace('', None).dropna().astype(float).describe())

    # print(df[df['Hogwarts House'] == 'Gryffindor'])

    # plt.hist(df[df['Hogwarts House'] == 'Gryffindor']["Arithmancy"])
    # plt.show()

    # print(df["Defense Against the Dark Arts"].astype(float))

    # loader.display(df.head())
 
    # prep = Preprocessing(df)
    # print(prep.split_by_house("Defense Against the Dark Arts"))
    # incepect_data = prep.inspect_data("Astronomy")
    # print(incepect_data)
 
 
if __name__ == "__main__":
    main()

# Arithmancy