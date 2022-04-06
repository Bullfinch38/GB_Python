# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

dir_name = 'my_project'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

folders = ['settings', 'mainapp', 'adminapp', 'authapp']

for f in folders:
    folder = os.path.join(dir_name, f)
    os.makedirs(folder)
#######################################################################################################################
    # to_remove = 'my_project'
    # if os.path.exists(to_remove):
    #     os.rmdir(to_remove)

    # dir_path = os.path.join('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
    # if not os.path.exists(dir_path):
    #     os.makedirs(dir_path)

    # to_remove = 'my_project'
    # if os.path.exists(to_remove):
    #     shutil.rmtree(to_remove)

