#! /bin/python3
import json
import os

def create_summary(base='.', exclude_dir=['docs', '_book', 'node_modules', 'images']):
    text = '# Summary\n'
    book_path = os.path.join(base, 'book.json')
    with open(book_path, 'r', encoding='utf-8') as f:
        js = json.load(f)
        intro = js['structure']['readme']
        text += '\n* [{}]({})\n'.format('简介', intro)
        
    for dir_ in os.listdir(base):
        if dir_ in exclude_dir or dir_.startswith('.'):
            continue
        path_ = os.path.join(base, dir_)
        if os.path.isfile(path_):
            continue
#         print(dir_)
        files = list(filter(lambda f: f.endswith('.md'), os.listdir(path_)))
        if 'README.md' in files:
            text += '\n* [{}]({})'.format(dir_, dir_+'/README.md')
        else:
            for f in files:
                if f.lower()[:-3]==dir_:
                     text += '\n* [{}]({})'.format(dir_, dir_+'/'+f)
                     break
            else:
                text += '\n* {}'.format(dir_)
            
#         print(files)
        files = list(filter(lambda f: f!='README.md' and f.lower()[:-3]!=dir_ , files))      
#         print(files)
        for f in files:
            text += '\n  * [{}]({})'.format(f[:-3], dir_+'/'+f)
        text += '\n\n---\n'
    with open(os.path.join(base, 'SUMMARY.md'), 'w', encoding='utf-8') as f:
        f.write(text)
#     print(text)

if __name__=='__main__':
    create_summary()
    print('over!')