def parser():
    game_ids = set()
    compteur = 0
    with open("./input.txt", "r") as outfile:
        data = outfile.readlines()
    for line in data:
        fewPerColor = { "red": 0, "green": 0, "blue": 0}
        if line.startswith("Game"):
            parts = line.split(":")
            if len(parts) == 2:
                game_id_str, game_data_str = parts
                game_id = int(game_id_str.split()[1])
                game_valid = True
                color_data_parts = [part.strip() for part in game_data_str.replace(",", ";").split(';')]
                for color_data in color_data_parts:
                    color_counts = [int(count) for count in color_data.split() if count.isdigit()]
                    color_words = [word.lower() for word in color_data.split() if word.isalpha()]
                    if len(color_counts) == len(color_words):
                        for count, word in zip(color_counts, color_words):
                            if word == "red" and count > fewPerColor["red"]:
                                fewPerColor["red"] = count
                            elif word == "green" and count > fewPerColor["green"]:
                                fewPerColor["green"] = count
                            elif word == "blue" and count > fewPerColor["blue"]:
                                fewPerColor["blue"] = count
                print(fewPerColor)
                compteur = compteur + (fewPerColor["red"] * fewPerColor["green"] * fewPerColor["blue"])
    return compteur
  

def main():
    zebi = parser()
    print(zebi)
    

if __name__ == "__main__":
    main()