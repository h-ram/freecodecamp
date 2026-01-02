def rock_paper_scissors(player1, player2):
    verdict = ""
    if player1 == player2:
        verdict = "Tie"
    elif player1 == "Rock" and player2 == "Scissors" or \
         player1 == "Paper" and player2 =="Rock" or \
         player1 == "Scissors" and player2 == "Paper":
        verdict = "Player 1 wins"
    else:
        verdict = "Player 2 wins"
    return verdict



test1 = rock_paper_scissors("Rock", "Rock")
test2 = rock_paper_scissors("Rock", "Paper")
test3 = rock_paper_scissors("Scissors", "Paper")
test4 = rock_paper_scissors("Rock", "Scissors")
test5 = rock_paper_scissors("Scissors", "Scissors")
test5 = rock_paper_scissors("Scissors", "Scissors")
test6 = rock_paper_scissors("Scissors", "Rock")

check1 = "Tie"
check2 = "Player 2 wins"
check3 = "Player 1 wins"
check4 = "Player 1 wins"
check5 = "Tie"
check6 = "Player 2 wins"


print(f"Test1: {test1==check1}")
print(f"Test2: {test2==check2}")
print(f"Test3: {test3==check3}")
print(f"Test4: {test4==check4}")
print(f"Test5: {test5==check5}")
print(f"Test6: {test6==check6}")
