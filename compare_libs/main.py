import os
import zipfile
import shutil

def read_list_from_file(filename):
    with open(filename, 'r') as f:
        #text_raw = f.readlines() # Need to cut '\n' and whitespaces for each element
        text_whole = f.read()
    text = text_whole.split(' \n')
    return text

def read_files_from_archive(archive_name):
    workdir = 'extracted'
    shutil.rmtree(workdir, ignore_errors=True)
    with zipfile.ZipFile(archive_name, 'r') as archive:
        archive.extractall(workdir)
    lib_files = [filename.rstrip('.lib') for filename in os.listdir(workdir) if filename.endswith('.lib')]
    if not lib_files:
        lib_files = [filename.rstrip('.a').lstrip('lib') for filename in os.listdir(workdir) if filename.endswith('.a')]
    print(lib_files)
    print(len(lib_files))
    shutil.rmtree(workdir)
    return set(lib_files)


def compare_archive(archive_name, filename='example_list.txt'):
    example_libraries = set(read_list_from_file(filename))
    print(f'Total number of Librarirs to search: {len(example_libraries)}')

    new_libraries = read_files_from_archive(archive_name)
    print(f'Total number of libs in out archive: {len(new_libraries)}')

    missing_libs = list(example_libraries.difference(new_libraries))
    missing_libs.sort()
    message = f'Total {len(missing_libs)} files missing  for archive {archive_name} \n Missing libraries:'
    with open(str(archive_name.rstrip('.zip') + "_report.txt"), 'w+') as f:
        f.write(message + ' \n')
        for line in missing_libs:
            f.write(f' - {line}')
            f.write(' \n')
    return

if __name__ == '__main__':
    compare_archive('example_lib.zip')