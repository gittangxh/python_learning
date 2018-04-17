import pickle

#file name for data storage
shoplistfile = 'shoplist.data'

# shoplist for purchasing
shoplist = ['apple', 'mango', 'carrot']

#ready to write
f = open(shoplistfile, 'wb')
#store the object to file
pickle.dump(shoplist,f)

f.close()

#clear shoplist varibles
del shoplist

#re-open the file
f=open(shoplistfile,'rb')
#load the object from file
storedlist = pickle.load(f)
print(storedlist)
