
HOUSE_COLUMN = "Hogwarts House"
HOUSES = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
HOUSE_COLORS = {
    "Gryffindor": "#740001",
    "Hufflepuff": "#ecb939",
    "Ravenclaw": "#0e1a40",
    "Slytherin": "#1a472a",
}
 


def is_number(value):
    try:
        num = float(value)
        return not math.isnan(num)
    except (ValueError, TypeError):
        return False
 
 
def get_numeric_columns(df, exclude=("Index",)):
    numeric_columns = []
    for column in df.columns:
        if column in exclude or column == HOUSE_COLUMN:
            continue
        values = df[column].dropna()
        if len(values) == 0:
            continue
        numeric_values = [v for v in values if is_number(v)]
        if len(numeric_values) > 0:
            numeric_columns.append(column)
    return numeric_columns


def get_values_by_house(df, column):
    """
    Retourne un dict {house: [valeurs numeriques de la colonne pour cette maison]}
    """
    result = {house: [] for house in HOUSES}
    print(result)
 
    for house in HOUSES:
        subset = df[df[HOUSE_COLUMN] == house]
        values = [
            float(v) for v in subset[column]
            if is_number(v)
        ]
        result[house] = values
 
    return result

def plot_histogram(df, column, ax=None, show=True):
    """
    Affiche un histogramme superposant les 4 maisons pour une matiere donnee.
    """
    values_by_house = get_values_by_house(df, column)
    

