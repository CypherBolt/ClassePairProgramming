import os

highscore_file = "highscore.txt"

def load_high_score():
    if os.path.exists(highscore_file):
        with open(highscore_file) as f:
            return int(f.read().strip() or 0)
    return 0

def save_high_score(value):
    with open(highscore_file, "w") as f:
        f.write(str(value))

high_score = load_high_score()

#when score changes:
if score > high_score:
    high_score = score
    save_high_score(high_score)
