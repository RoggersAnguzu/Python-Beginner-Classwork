f = open('mystory2.txt', 'w')
story = "Once upon a time\nthere was a drought."
story = story + "The animals got together\n"
story = story + "to dig a well.\nThe End."

f.write(story)
f.close()