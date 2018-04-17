import os
import time
import zipfile

source = ['C:\\Users\\wan\\Documents\\source']
target_dir='D:\\Backup' + '\\' + time.strftime('%Y%m%d')

comment = input('Please enter a comment -->')

print(source)

zip_name=time.strftime('%H%M%S')

if len(comment) != 0:
    zip_name=zip_name+'_'+comment.replace(' ','_')+'.zip'
else:
    zip_name=zip_name + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# zip_command= '7z a {0} {1}'.format(target, ''.join(source))
#
# print('zip command is:', zip_command)
#
# print('running...')
#
# if os.system(zip_command) == 0:
#     print('sucessfully backup to', target)
# else:
#     print('backup failed')

azip = zipfile.ZipFile(target_dir+'\\'+zip_name, 'w')
if os.path.isdir(''.join(source)):
    for eachfile in os.listdir(''.join(source)):
        azip.write(''.join(source)+'\\'+eachfile)
azip.close()
