import json
import matplotlib.pyplot as plt 
'''
/Users/joellemin/Downloads/HW02cs/country.json
'''

with open('/Users/joellemin/Downloads/senator.json','r') as p:
    senator_file = json.load(p)
'''
# print("\n")
counts1 = {'Democrat': 0, 'Republican': 0, 'Independent': 0}

for key, value in counts.items():
    for i in range(len(senator_file['objects'])):
        if key == senator_file['objects'][i]['party']:
            counts[key] += 1
'''
#{'Democrat': 45, 'Republican': 53, 'Independent': 2}


counts2 = {'class1': 0, 'class2': 0, 'class3': 0}

for key, value in counts2.items():
    for i in range(len(senator_file['objects'])):
        if key == senator_file['objects'][i]['senator_class']:
            counts2[key] += 1

labels = 'class1', 'class2', 'class3'
sizes = [33, 33, 34]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
#{'class1': 33, 'class2': 33, 'class3': 34}
"""
'''
fig, [ax1, ax2] = plt.subplots(2)
ax1.set(xlabel='these are the words')
ax1.set(ylabel='the number of times Trump tweeted the word')
ax1.bar( counts.keys() , counts.values() )
ax2.bar( [1,2,3], [4,3,2] )
#plt.show()
'''
fig, ax = plt.subplots()
ax.set(
    xlabel='Party Label',
    ylabel='Number of Senators',
    )
x = list(counts1.keys())
# heights = sorted(counts1.values())
heights = []
for label in x:
    heights.append(counts1[label])

#print('heights=',heights)

ax.bar( x , heights )
plt.show()

# .keys() is non-deterministic
# sorted(counts.keys()) is deterministic
#print('counts.keys()=',sorted(counts.keys()))
"""
