from .PomParser import PomParser
import xml.etree.ElementTree as ET


class ChildPomParser(PomParser):

    def __init__(self, pom_file):
        # print(pom_file)
        super(ChildPomParser, self).__init__(pom_file)
        self.is_root = False

    def is_core_pom(self):
        if self.is_jar_pom() and self.find_node(self.root_node, "parent") is not None:
            return True
        else:
            return False

    def get_core_installing_path(self):
        """
        core install path: where the project jars are in.
        :return:
        """
        if not self.is_core_pom():
            return None
        return self.get_installing_path()
