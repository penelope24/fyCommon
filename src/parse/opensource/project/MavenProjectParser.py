from src.file.Traverse import Traverse
from .ProjectParser import ProjectParser


class MavenProjectParser(ProjectParser):
    """
    parse properties at project level.
    always make sure the project is maven project before using this class
    """
    def __init__(self, path):
        super(MavenProjectParser, self).__init__(path)
        self.root_pom = self._get_root_pom()
        self.root_build_path = "/".join(self.root_pom.split("/")[:-1])

    def _get_root_pom(self):
        """
        since os.walk() walks in a top-down mode, the first returned pom file is always root.
        :return: the root pom file path of current project
        """
        for i in range(4):
            t= Traverse(self.path)
            check_files = t.list_files_by_depth(i, abs=True)
            for file in check_files:
                if str(file).split("/")[-1] == "pom.xml":
                    return file
        return None

    def get_all_poms(self, depth=5):
        """
        get all pom files other than the root pom, in a rather save range of search depth.
        :param depth: search depth
        :return: searched pom files
        """
        t = Traverse(self.path)
        # first set root pom file
        pom_files = []
        for i in range(depth):
            pom_files.extend(t.find_files_by_depth("pom.xml", i))
        return pom_files

