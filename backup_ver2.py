import os
import time

source = ['C:\\Users\\wan\\Documents\\source']
target_dir='D:\\Backup' + '\\' + time.strftime('%Y%m%d')

comment = input('Please enter a comment -->')

print(source)

if len(comment) != 0:
    target=target_dir+'\\'+time.strftime('%H%M%S')+'_'+comment.replace(' ','_')+'.zip'
else:
    target=target_dir+'\\'+time.strftime('%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)



zip_command= '7z a {0} {1}'.format(target, ''.join(source))

print('zip command is:', zip_command)

print('running...')

if os.system(zip_command) == 0:
    print('sucessfully backup to', target)
else:
    print('backup failed')
