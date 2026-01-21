words=['cat', 'dog', 'cow', 'camel']
group={}

d=dict()
for word in words:
    key=word[0]
    d.setdefault(key,[].append(word))

print(d)
