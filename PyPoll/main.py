import csv
Total_votes = 0
candidates_names = []
candidates_votes ={}



with open ('Resources/election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        
        Total_votes += 1
    
        candidates_name = row[2]
        
        if candidates_name not in candidates_names:
            candidates_names.append(candidates_name)
            candidates_votes[candidates_name] = 0
        candidates_votes[candidates_name] += 1

#print final votes to terminal


percentages = {key: round(val / Total_votes *100,3)for key,val in candidates_votes.items()}


winning_candidate = max(candidates_votes, key=candidates_votes.get)


with open ('analysis/election_analysis.txt', 'w') as txtfile:

    output1=(
    f'Election Results\n'
    f'-------------------------\n'
    f'Total Votes: {Total_votes}\n'
    f'-------------------------\n'

    )
    txtfile.write(output1)
    print(output1)
    for k, v in candidates_votes.items():
        output2 = (f'{k}: {percentages[k]}% ({v})\n')
        print(output2)
        txtfile.write(output2)


    output3=(
    f'-------------------------\n'
    f'Winner: {winning_candidate}\n'
     f'-------------------------'
    )
    print(output3)
    txtfile.write(output3)


