from core.data_structure import *
from core.drawing import *


if __name__ == "__main__":
    data = load_parsing_data()
    
    plot_accident_type_by_year(data)