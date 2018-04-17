poem = '''\
Programming is fun
When the work is done
If you anna make your work also fun:
    use Python!
'''


#open the file with 'w'riting
f=open('poem.txt','w')
#write text into txt file
f.write(poem)
#close the file
f.close()

f=open('poem.txt','r')
while True:
    line=f.readline()
    if len(line) == 0:
        break
    print(line,end='')

f.close()
