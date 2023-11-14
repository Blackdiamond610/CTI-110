# CTI-110
# P4HW1
# Josh A.
# 11/2/23

def calculate_average_score(score_list):
    if len(score_list) > 1:
        min_score = min(score_list)
        score_list.remove(min_score)
    average_score = sum(score_list) / len(score_list)
    return average_score

def determine_letter_grade(average_score):
    if average_score >= 90:
        return 'A'
    elif 80 <= average_score < 90:
        return 'B'
    elif 70 <= average_score < 80:
        return 'C'
    elif 60 <= average_score < 70:
        return 'D'
    else:
        return 'F'

def main():
    scores = []
    num_scores =int(input("Enter the number of scores you would like to enter: "))
    while num_scores <= 0:
        print("Please enter a valid number of scores greater than 0.")
        num_scores =int(input("Enter the number of scores you would like to enter: "))

    for i in range(num_scores):
        valid_score = False
        while not valid_score:
            score = float(input(f"Enter score {i + 1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                valid_score = True
            else:
                print("Invalid score. Please enter a score between 0 and 100.")
    
    average = calculate_average_score(scores)
    letter_grade = determine_letter_grade(average)
    min_score = min(scores)
    print("Results: ")
    print("lowest score:",min_score)
    print("Scores entered:", scores)
    print("Average score:", average)
    print("grade:", letter_grade)

if __name__ == "__main__":
    main()

