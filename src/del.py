import os.path

def delete_pyc(dir_path):
    
    counter = 0
    for pyc_path, dirs, files in os.walk(dir_path):
        for pyc_file in files:
            if pyc_file[-4:] == '.pyc':
                #print(pyc_file)
                full_path = os.path.join(pyc_path, pyc_file)
                #print(full_path)
                os.remove(full_path)
                counter += 1

    print("Deleting .pyc process... " + str(counter) + " files removed.")

if __name__ == '__main__':
    delete_pyc('.')