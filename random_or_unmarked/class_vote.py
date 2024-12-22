class_name = input("Name of class: ")
num_of_students = int(input("Number of students in class: "))
num_of_candidates = int(input("Number of candidates: "))
names_of_candidates = input(
    "Enter names of candidates separated with a comma and a space: ")

running = True
candidates = names_of_candidates.split(", ") + ["Abstain"]

while running:
    vote_count = [0] * (num_of_candidates + 1)
    for _ in range(num_of_students):
        print(
            f"\nEach student will now place their votes from the following choice:\n{candidates}")
        vote_prompt = f"Enter your choice from 1 to {len(candidates)}: "
        vote = int(input(vote_prompt))
        vote_count[vote - 1] += 1

    max_votes = max(vote_count)
    winners = []

    print(f"\n{class_name}")
    for i in range(num_of_candidates):
        if vote_count[i] == max_votes:
            winners.append(candidates[i])
        print(f"{candidates[i]}: {vote_count[i]} votes")
    print(f"{winners} won the election.")

    if len(winners) > 1:
        print("\nThere has been a tie in the election. Re-voting will begin.")
        candidates = winners + ["Abstain"]
    else:
        running = False
