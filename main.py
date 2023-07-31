cand_list = []
cand_num_list=[]

cand_1=0
cand_2=0
cand_3=0
cand_4=0

cand_num = int(input("Total candidates >>>"))
if cand_num > 4:
  print("You can only have 4 candidates")
elif cand_num < 2:
  print("You must have more than 2 candidates")

else:
  for i in range (cand_num):
    name = input("Input your candidate name >>>")
    cand_list.append(name)
    cand_num_list.append((name,i+1))
print(cand_list)
print(cand_num_list)

for i in range(1,4):
  votes = int(input(f"Enter a number between 1 and {cand_num} to vote for your participant >>>"))

  if votes == 1:
    cand_1 +=1

  elif votes == 2:
    cand_2 +=1

  elif votes == 4:
    cand_3 +=1

  elif votes == 4:
    cand_4 +=1

  else:
    print("Invalid candidate number")

print(cand_list[0]," has ",cand_1," votes.")
print(cand_list[1]," has ",cand_2," votes.")
print(cand_list[2]," has ",cand_3," votes.")
print(cand_list[3]," has ",cand_4," votes.")
