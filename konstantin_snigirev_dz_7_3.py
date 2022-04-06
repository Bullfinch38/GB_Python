import os
import shutil

dir_name = 'my_project_2'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

folders = ['settings', 'adminapp', 'templates', 'authapp']

for f in folders:
    folder = os.path.join(dir_name, f)
    os.makedirs(folder)

a = shutil.move('my_project_2/adminapp', 'my_project_2/templates')
b = shutil.move('my_project_2/authapp', 'my_project_2/templates')

# a = shutil.move('my_project_2/adminapp', 'my_project_2/templates')
# b = shutil.move('my_project_2/authapp', 'my_project_2/templates')
# os.makedirs('my_project_2/templates/{}'.format(folders_template), exist_ok=True)



