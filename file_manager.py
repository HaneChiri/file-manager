import os
import shutil
import yaml
import logging

logging.basicConfig(level=logging.INFO)

# 加载设置
with open('settings.yml', 'r',encoding='utf-8') as f:
    data = yaml.safe_load(f.read())

    collect_list = data['collect_list']
    source_path_list = collect_list['source']
    destination_path = collect_list['destination']
    except_file_list = collect_list['except_file']

    logging.info('source:' + str(source_path_list))
    logging.info('destination:' + str(destination_path))
    logging.info('except_files:' + str(except_file_list))

file_num = 0
for source_path in source_path_list:
    file_list = [ file for file in os.listdir(source_path) if file[0] != '.' and file not in except_file_list]

    for file in file_list:
        source = source_path+'\\'+file
        destination = destination_path+'\\'+file
        shutil.move(source,destination) # 移动文件
        logging.info('[{}]->[{}]'.format(source,destination))
    
    file_num += len(file_list)

logging.info('成功移动{}个文件至{}'.format(file_num,destination_path))
os.system('pause')