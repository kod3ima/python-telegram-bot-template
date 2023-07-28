import os

def get_directory_tree(root_path, indent=''):
    tree = ""

    files = os.listdir(root_path)

    files.sort()

    for file in files:
        current_path = os.path.join(root_path, file)

        if os.path.isdir(current_path):
            tree += f"{indent}+ {file}/\n"
            tree += get_directory_tree(current_path, indent + '  ')
        else:
            tree += f"{indent}- {file}\n"

    return tree
