import os
import json
import subprocess

with open(r'C:\Users\Steph\Desktop\mahsa.txt', 'a+') as f:
  
  t = f.readlines()
  #t.remove(t[2])
  print (t)
  #to_delete = input('What should we delete? : ')
  f.seek(0,2)
  for line, j in enumerate(t):
    print ('line = ', line, 'j = ',j)
    #f.truncate()

process = os.popen(r'C:\Users\Steph\Desktop\mahsa.txt')
a = process.read()
print (a)

def filerev(somefile, buffer=0x20000):
  somefile.seek(0, os.SEEK_END)
  size = somefile.tell()
  return size

size = filerev(open(r'C:\Users\Steph\Desktop\mahsa.txt'))
#print(size)

f = open(r'C:\Users\Steph\Desktop\mahsa.txt')
#f.seek(0, 2)
f.seek(-1, 2)
print(f.read(1))

# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })
# with open(r'C:\Users\Steph\Desktop\data.txt', "w") as write_file:
#     json.dump(data, write_file)
#
# with open(r'C:\Users\Steph\Desktop\data.txt') as json_file:
#     data = json.load(json_file)
#     for p in data['people']:
#         print('Name: ' + p['name'])
#         #print('Website: ' + p['website'])
#         #print('From: ' + p['from'])
#         #print('')
#
# with open(r'C:\Users\Steph\Desktop\data.txt', "w") as f:
#   #outputArea.insert("1.0", the_file.read())
#   for i in range(5):
#     f.write("This is line %d\r\n" % (i + 1))
#
#
#
# with open(r'C:\Users\Steph\Desktop\data.txt', "r") as f:
#   if f.mode == 'r':
#     contents =f.read()
#     print (contents)
#
