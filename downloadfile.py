import requests


def download_file(url,local_filename):

    # local_filename = '/root/orangepizero/update.zip'
    # NOTE the stream=True parameter
    print(local_filename)    
    r = requests.get(url, stream=True)
    print(r.iter_content)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                # f.flush() commented by recommendation from J.F.Sebastian
    print(r)
    return local_filename
# path = ''
# download_file(
#     'http://solardata.tk/build/download?build=1',path+'update.zip')

