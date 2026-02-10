import csv
import json
with open("config.txt" , "r", encoding="utf-8") as f:
    min = int(f.read())

print("мін бал:", min)

list = []

with open("students.csv", "r" , encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
            r["score"] = int(r["score"])
            list.append(r)

retest = []

for i in list:
    if i["score"]< min:
        retest.append(i)

with open("retest.csv", "w", newline="", encoding="utf-8") as f:
    name = ["id" , "name", "surname", "score"]
    writer =csv.DictWriter(f, fieldnames=name)

    writer.writeheader()
    for i in retest:
        writer.writerow(i)


list2 = []
for i in list:
    if i["score"]>= min:
        i["pass"] = True
        list2.append( i)

with open("best_students.json", "w", encoding="utf-8") as f:
    json.dump(list2,f, indent=4, ensure_ascii=False)
