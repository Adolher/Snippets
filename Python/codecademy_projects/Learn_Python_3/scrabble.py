letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {k:v for k, v in zip(letters, points)}
letter_to_points[""] = 0

def score_word(word):
    sum = 0
    for l in word:
        sum += letter_to_points.get(l.upper(),0)
    return sum

def play_word(d, player, word):
    d.get(player).append(word)

def calculate(d, l):
    for k, v in d.items():
        player_sum = 0
        for w in v:
            player_sum += score_word(w)
        l[k] = player_sum

brownie_points = score_word("Brownie")

player_to_words = {"player1": ["BLUE","TENNIS","EXIT"], "wordNerd": ["EARTH","EYES","MACHINE"],
    "Lexi Con": ["ERASER","BELLY","HUSKY"], "Prof Reader": ["ZAP","COMA","PERIOD"]}
player_to_points = {}

calculate(player_to_words, player_to_points)
print(player_to_points)

play_word(player_to_words, "player1", "Further")

calculate(player_to_words, player_to_points)
print(player_to_points)