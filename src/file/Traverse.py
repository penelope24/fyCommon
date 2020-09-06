"""
methods about list directories and files.
"""
import os


class Traverse:

    def __init__(self, path):
        self.path = path

    def list_dirs_by_depth(self, depth, abs=False):
        """
        list all directories at certain depth
        """
        res = []
        path = os.path.normpath(self.path)
        for root, dirs, files in os.walk(path):
            dep = root[len(path):].count(os.path.sep)
            if dep == depth:
                if abs:
                    res += [os.path.join(root, d) for d in dirs if not d.startswith(".")]
                else:
                    res += [d for d in dirs if not d.startswith(".")]
                dirs[:] = []
        return res

    def list_files_by_depth(self, depth, abs=False):
        """
        list all files at certain depth
        """
        res = []
        path = os.path.normpath(self.path)
        for root, dirs, files in os.walk(path):
            dep = root[len(path):].count(os.path.sep)
            if dep == depth:
                if abs:
                    res += [os.path.join(root, f) for f in files if not f.startswith(".")]
                else:
                    res += [f for f in files if not f.startswith(".")]
                dirs[:] = []
        return res

    def find_files_by_depth(self, target_file_name, depth, abs=True):
        """
        find file pf certain name at given depth
        :param target_file_name:
        :param abs:
        :return: by default return full path
        """
        res = []
        path = os.path.normpath(self.path)
        for root, dirs, files in os.walk(path):
            dep = root[len(path):].count(os.path.sep)
            if dep == depth:
                if abs:
                    res += [os.path.join(root, f) for f in files if str(f) == "pom.xml"]
                else:
                    res += [f for f in files if str(f) == "pom.xml"]
                dirs[:] = []
        return res
