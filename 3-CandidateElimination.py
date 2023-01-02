import csv

with open("trainingexamples.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

    specific = data[0][:-1]
    general = [['?' for i in range(len(specific))] for j in range(len(specific))]

    for row in data:
        if row[-1] == "Yes":
            for i in range(len(specific)):
                if row[i] != specific[i]:
                    specific[i] = "?"
                    general[i][i] = "?"

        elif row[-1] == "No":
            for i in range(len(specific)):
                if row[i] != specific[i]:
                    general[i][i] = specific[i]
                else:
                    general[i][i] = "?"

        print("\nStep " + str(data.index(row)+1) + " of Candidate Elimination Algorithm")
        print(specific)
        print(general)

    gh = [] # gh = general Hypothesis
    for row in general:
        for i in row:
            if i != '?':
                gh.append(row)
                break
    print("\nFinal Specific hypothesis:\n", specific)
    print("\nFinal General hypothesis:\n", gh)