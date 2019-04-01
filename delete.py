import os


def delete(path):
    try:
        os.remove(path)
    except OSError as e:  # if failed, report it back to the user ##
        print("Error: %s - %s." % (e.filename, e.strerror))
