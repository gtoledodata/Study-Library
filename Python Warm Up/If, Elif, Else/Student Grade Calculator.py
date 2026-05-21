# Student Grade Calculator
score_1 = float(input("Enter the first score: "))
score_2 = float(input("Enter the second score: "))
score_3 = float(input("Enter the third score: "))

mean_score = (score_1 + score_2 + score_3) / 3

if mean_score >= 70:
    print("Congratulations! You passed the course.")
elif 50 <= mean_score < 70:
    print("You need to improve your grades.")
else:
    print("Sorry, you failed the course.")
    
    