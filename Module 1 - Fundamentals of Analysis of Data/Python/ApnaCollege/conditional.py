# Ternary Operator
food = "rice"
eat = "yes" if food == "rice" else "no"
print(eat)
# Output: yes

food = "cake"
print("sweet") if food == "cake" or food == "jalebi" else print("salty")
# Output: sweet

age = 19
vote = ("yes", "no")[age < 18]
print(vote)
#output: yes

sal = 1000
tax =sal*(0.1,0.2)[sal>1000]
print(tax)
#output: 200.0
