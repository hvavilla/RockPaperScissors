
from Winner import Winner

def main():
    winner = Winner()
    winner.getInputFromUsers()
    winner.deterMineWinner()

if __name__ == "__main__":
    play = "Y"
    while (True):        
        play = play.upper()
        if (play == "N"):
           break
        else:
           main()
           play = input("Play Again ? Y or N:")
