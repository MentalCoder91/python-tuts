scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 100, 200, 150, 20, 203, 105]

total_score = sum(scores)
print(f"Using inbuilt: {total_score}")

sum = 0
for score in scores:
    sum += score
print(f"using for loop : {sum}")

total_score_max = max(scores)
print(f"max score using function is :{total_score_max}")

max = -1
for score in scores:
    if score >= max:
        max = score
print(f"max using loops : {max}")
