def get_anthill() -> str:
    input_map = input("Which anthill would you pick ? \n 0 \n 1 \n 2 \n 3 \n 4 \n 5 \n Your choice: ")
    match input_map:
        case "0":
            return "fourmiliere/fourmiliere_zero.txt"
        case "1":
            return "fourmiliere/fourmiliere_un.txt"
        case "2":
            return "fourmiliere/fourmiliere_deux.txt"
        case "3":
            return "fourmiliere/fourmiliere_trois.txt"
        case "4":
            return "fourmiliere/fourmiliere_quatre.txt"
        case "5": 
            return "fourmiliere/fourmiliere_cinq.txt"
        case _:
            return ValueError(f"Invalid input , try to choose from the options: {input_map} ")
