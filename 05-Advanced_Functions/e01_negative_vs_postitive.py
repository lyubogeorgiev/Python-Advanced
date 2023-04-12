numbers = [int(x) for x in input().split()]

negatives = [x for x in numbers if x < 0]
positives = [x for x in numbers if x >= 0]

negatives_sum = sum(negatives)
positives_sum = sum(positives)

stronger = ("negatives", "positives") if abs(negatives_sum) > positives_sum else ("positives", "negatives")

print(negatives_sum)
print(positives_sum)
print(f'The {stronger[0]} are stronger than the {stronger[1]}')