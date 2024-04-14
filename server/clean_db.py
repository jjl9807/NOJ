import os


def clean_migrations(directory):
    # 遍历给定目录
    for root, dirs, files in os.walk(directory):
        # 检查目录名是否为 'migrations' 且不是空目录
        if 'migrations' in dirs:
            migrations_path = os.path.join(root, 'migrations')
            # 遍历 'migrations' 目录中的文件
            for filename in os.listdir(migrations_path):
                file_path = os.path.join(migrations_path, filename)
                # 保留 '__init__.py'，删除其他文件
                if filename != '__init__.py' and os.path.isfile(file_path):
                    os.remove(file_path)
                    print(f'Removed {file_path}')


# 指定你项目的顶级目录
project_directory = os.getcwd()
clean_migrations(project_directory)
