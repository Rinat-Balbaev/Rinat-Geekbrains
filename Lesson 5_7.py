import json
import codecs
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with codecs.open('test_7.txt', 'r', "utf_8_sig") as file:
    for line in file:
        name, form, revenue, costs = line.split()
        profit[name] = int(revenue) - int(costs)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Average profit - {prof_aver:.2f}')
    else:
        print(f'No profit')
    pr = {'Average profit': round(prof_aver)}
    profit.update(pr)
    print(f'Profit for each company - {profit}')

with open('test_7.json', 'w') as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'JSON file created with following contents: \n '
          f' {js_str}')