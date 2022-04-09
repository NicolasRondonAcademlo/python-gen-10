
jon_snow =["Jon Snow", "Winterfell", 30]
print(jon_snow)
print(type(jon_snow))
print(jon_snow[len(jon_snow) -1])
###

jon_snow[2] += 30
print(jon_snow[2])
jon_snow[0] = "jon"
print(jon_snow)

#name = "Maria"
#name[0]="N"

num_seq = range(0,11,3)
num_seq = list(num_seq)
print(num_seq)

# List-Ception
world_cup_winners = [
    [2006, "Italy"], [2010, "Spain"],
    [2014, "Germany"], [1986, "Argentina"]
]
print(world_cup_winners)

print(world_cup_winners[-1][-1])

part_a = [1,2,3,4,5,6]
part_b = [6,7,8,9,10]
merged_list = part_a + part_b
print(merged_list)

part_A = [1,2,3,4,5,6]
part_B = [6,7,8,9,10]

part_A.extend(part_B)

