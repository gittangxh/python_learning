import os
import time

source = ['C:\\Users\\wan\\Documents\\source']
target_dir='D:\\Backup'

print(source)
target=target_dir+'\\'+time.strftime('%Y%m%d%H%M%S')+'.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command= '7z a {0} {1}'.format(target, ''.join(source))

print('zip command is:', zip_command)

print('running...')

if os.system(zip_command) == 0:
    print('sucessfully backup to', target)
else:
    print('backup failed')
