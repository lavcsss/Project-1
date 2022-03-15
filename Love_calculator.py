from itertools import count

print('''
       /:""|  .@@@@@,
(\/)  |:`66|_ @@@@@@@@,
 \/   C`    _)aa`@@@@@@
       \ ._| (_   ?@@@@
        ) /   =' @@@@"
       /`\\    \(```
      || |Y|  //`\
      || |.| / | || (\/)
      || |.| \ | ||  \/
      || |.|  \| ||
      :| |=:   |_|\
      ||_|,|   |_| \
      \)))||   (((  |
 (\/)  |  ||   |____|
  \/   |  ||   |____|
       >  ))    | ||
       | ||     | ||
       | ||     | ||
       |_||__   /~))
  jgs  (____)) /_/YY
''')
string_1 = input("Enter your name").lower()
string_2 = input("Enter your Lover's name").lower()
total_count_1 = 0
total_count_2 = 0
for i in "true":
    count_1 = (string_1 + string_2).count(i)
    total_count_1 += count_1
print(total_count_1)

for j in "love":
    count_2 = (string_1 + string_2).count(j)
    total_count_2 += count_2
print(total_count_2)
total_count = total_count_1 * 10 + total_count_2 

print(f"Your score is{total_count}", end= " ")
if total_count <10 or total_count > 90:
    print(", you go together like coke and mentos.")
elif total_count >=40 and total_count <=50:
    print(", you are alright together")
else:
    pass
    