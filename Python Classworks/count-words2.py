f = open('mystory.txt', 'r')
count = 0
story = f.read()
    
print("The file has", len(story.split()), "words.")   
print("The file has", len(story), 'characters.')