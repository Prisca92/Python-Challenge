import csv
months_list = []
amounts_list =[] 
change_list = []
greatest_decrease = []
greatest_increase = []
profit_losses = []
Monthly_profitloss = 0
previous_month = 1088983
output_text = []
Text_file=[]

with open ('Resources/budget_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
    
        months_list.append(row[0])
        amounts_list.append(int(row[1]))
        Monthly_profitloss = (int(row[1]))
        Change = Monthly_profitloss - previous_month
        previous_month = Monthly_profitloss
        change_list.append(Change)
        #print(change_list)
    total_months= len(months_list)
    total_net = sum(amounts_list)
    total_change = sum(change_list)
    greatest_increase = max(change_list)
    greatest_decrease = min(change_list)
    # print(f'total number of months in the dataset:{total_months}')
    # print(total_net)
    # print(amounts_list)
    # print(total_change)
    greatest_month = change_list.index(greatest_increase)
    least_month = change_list.index(greatest_decrease)
    #print(greatest_month)
    date_g = months_list[greatest_month]
    #print(date_g)
    #print(least_month)
    date_l = months_list[least_month]
    #print(date_l)
   
    average_change = round(sum(change_list) /(len(change_list)- 1),2)
    print('Finacial Analysis')
    print('----------------------------')
    print(f'Total Months: {total_months}')
    print(f'Total: ${total_net}')
    print(f'Average Change: ${average_change}')
    print(f'greatest_increase in profits:{date_g} {greatest_increase}')
    print(f'greatest_decrease in profits:{date_l}{greatest_decrease}')



    txt_output = (amounts_list,total_change)
with open ('analysis/budget_analysis.txt', 'w') as txtfile:
    txtfile.write('Finacial Analysis\n')
    txtfile.write('----------------------------\n')
    txtfile.write(f'Total Months: {total_months}\n')
    txtfile.write(f'Total: ${total_net}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write( f'greatest_increase in profits: {date_g} (${greatest_increase})\n')
    txtfile.write(f'greatest_decrease in profits: {date_l} (${greatest_decrease})')