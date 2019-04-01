from zipfile import ZipFile
import zipfile
# specifying the zip file name


def extractall(extract_path,zip_path):
    print(extract_path)
    print(zip_path)
    # opening the zip file in READ mode
    with ZipFile(extract_path, 'a') as zip:
        # printing all the contents pof the zip file
        zip.printdir()
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall(zip_path)
        print('Done!')
# extractall('','update.zip')

