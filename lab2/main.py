import pathlib


def search_file(filename_part: str = '',
                extension: str = '',
                path: pathlib.Path = None,
                recursive: bool = False) -> list[pathlib.Path]:
    # *filename*.extension
    if filename_part != '' and extension == '':
        pattern = str('*' + filename_part + '*' + '.*')
        print(pattern)
    elif filename_part == '' and extension != '':
        pattern = str('*.' + '*' + extension + '*')
        print(pattern)
    elif filename_part != '' and extension != '':
        pattern = str('*' + filename_part + '*' + '.' + '*' + extension + '*')
        print(pattern)
    else:
        pattern = str('*.*')
    results = list()

    if recursive:
        iterator = path.rglob(pattern)
    else:
        iterator = path.glob(pattern)

    for child in iterator:
        results.append(child)
    return results


def search_dir(dirname_part: str,
               path: pathlib.Path,
               recursive: bool) -> list[pathlib.Path]:
    # *dir_name_part*/
    if dirname_part != '':
        pattern = str('*' + dirname_part + '*/')
        print(pattern)
    else:
        pattern = str('*/')
        print(pattern)
    results = list()

    if recursive:
        iterator = path.rglob(pattern)
    else:
        iterator = path.glob(pattern)

    for child in iterator:
        results.append(child)
    return results


print()
print(search_file(filename_part='c',
                  extension='csv',
                  path=pathlib.Path('test_dir'),
                  recursive=True), end='\n\n')
print(search_file(filename_part='c',
                  path=pathlib.Path('test_dir'),
                  recursive=True), end='\n\n')
print(search_file(extension='csv',
                  path=pathlib.Path('test_dir'),
                  recursive=True), end='\n\n')
print(search_file(filename_part='c',
                  path=pathlib.Path('test_dir'),
                  recursive=True), end='\n\n')
print(search_file(filename_part='c',
                  extension='csv',
                  path=pathlib.Path('test_dir\second'),
                  recursive=False), end='\n\n')
print(search_file(path=pathlib.Path('test_dir'),
                  recursive=True), end='\n\n')
print(search_dir(dirname_part='se',
                 path=pathlib.Path('test_dir'),
                 recursive=True))
