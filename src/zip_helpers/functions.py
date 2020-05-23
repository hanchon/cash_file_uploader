from os.path import basename
from zipfile import ZipFile


def create_zip(files_path, name="sample2.zip"):
    # Create a ZipFile Object
    with ZipFile(name, 'w') as zipObj2:
        # Add multiple files to the zip
        for path in files_path:
            zipObj2.write(path, basename(path))