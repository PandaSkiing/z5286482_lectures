import os


def safe_open(pth, mode='rt'):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
        Defaults to 'rt'
    """
    if 'w' not in mode:
        # If the mode does not contain 'w', it's safe to open the file.
        return open(pth, mode)

    if os.path.exists(pth):
        # The file already exists, so we need to check its content.
        with open(pth, 'rt') as file:
            content = file.read()
            if len(content) == 0:
                # If the file is empty, it's safe to open it in write mode.
                return open(pth, mode)
            else:
                # The file has content, raise an Exception.
                raise Exception("File already exists and contains data. Cannot overwrite.")

    # If the file does not exist, it's safe to open it in write mode.
    return open(pth, mode)


if __name__ == "__main__":
    # Test cases
    # Opening an existing file with content for reading
    with safe_open("test_file_exists_with_content.txt", mode='r') as fobj:
        print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("test_file_exists_no_content.txt", mode='w') as fobj:
        fobj.write('content')

    # Opening an existing file with content for writing - should raise Exception
    try:
        with safe_open("test_file_exists_with_content.txt", mode='w') as fobj:
            fobj.write('content')
    except Exception as e:
        print(f"Exception: {e}")

import os

def safe_open(pth, mode='rt'):
    """ Opens the file in `pth` using the mode in `mode` and returns
    a file object.

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading,
        and 'a' for appending. See the `open` function for more options.
        Defaults to 'rt'
    """
    pass


if __name__ == "__main__":

    # Opening an existing file with content for reading
    with safe_open("test_file_exists_with_content.txt", mode='r') as fobj:
       print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("test_file_exists_no_content.txt", mode='w') as fobj:
       fobj.write('content')


    # Opening an existing file with content for writing - should raise Exception
    with safe_open("test_file_exists_with_content.txt", mode='w') as fobj:
       fobj.write('content')
