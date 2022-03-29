import hashlib
import os


class Md5Ui:

    @staticmethod
    def md5(fname):
        hash_md5 = hashlib.md5()
        with open(fname, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    @staticmethod
    def check_hash(hash1, hash2):
        return hash1 != hash2

    @staticmethod
    def save_hash(hash, filename):
        with open(filename, "w") as f:
            f.write(hash)

    @staticmethod
    def read_hash(filename):
        with open(filename, "r") as f:
            return f.read()

    @staticmethod
    def update_ui(filename_hash, filename_file):
        hash1 = Md5Ui.read_hash(filename_hash)
        hash2 = Md5Ui.md5(filename_file)
        if Md5Ui.check_hash(hash1, hash2):
            command = f"pyuic5 -o {os.path.join(os.path.dirname(filename_file), 'main_ui.py')} {filename_file}"
            os.system(command)
            Md5Ui.save_hash(hash2, filename_hash)
            # time.sleep(2)
