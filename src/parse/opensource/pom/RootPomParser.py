import os
import xml.etree.ElementTree as ET
from .PomParser import PomParser
from .ChildPomParser import ChildPomParser


class RootPomParser(PomParser):

    def __init__(self, pom_file):
        super(RootPomParser, self).__init__(pom_file)
        self.is_root = True
        self.root_build_path = "/".join(self.pom_file.split("/")[:-1])

    def is_core_pom(self):
        if self.is_jar_pom():
            return True
        if self.find_node(self.root_node, "modules") is None:
            return True
        return False

    def get_core_paths(self):
        """
        a core path has 3 key components:
        1. pom.xml
        2. deps/
        3. target/
        :return:
        """
        if self.is_root is False:
            return None
        node_modules = self.find_node(self.root_node, "modules")
        # if it's a single-module project
        if node_modules is None:
            core_path = self.root_build_path
            jar = self.get_jar_name()
            return [core_path + "$" + jar]
        # if it's a multi-module project and root pom is not core (packaging==pom)
        elif not self.is_core_pom():
            res = []
            for pom in self.get_all_submodules(self.root_build_path):
                if os.path.exists(pom) and ChildPomParser(pom).is_core_pom():
                    pom_parser = ChildPomParser(pom)
                    core_path = "/".join(pom_parser.pom_file.split("/")[:-1])
                    jar = pom_parser.get_jar_name()
                    res.append(core_path + "$" + jar)
            return res
        # a rare cae that it's a multi-module project and root pom is also core
        else:
            root_core_path = self.root_build_path
            root_jar = self.get_artifact_id()
            res = []
            res.append(root_core_path + "$" + root_jar)
            for pom in self.get_all_submodules(self.root_build_path):
                if os.path.exists(pom) and ChildPomParser(pom).is_core_pom():
                    pom_parser = ChildPomParser(pom)
                    core_path = "/".join(pom_parser.pom_file.split("/")[:-1])
                    jar = pom_parser.get_jar_name()
                    res.append(core_path + "$" + jar)
            return res

    def get_all_submodules(self, root):
        all_module_poms = []
        root_pom_file = root + "/pom.xml"
        root_node = ET.parse(root_pom_file).getroot()
        node_modules = self.find_node(root_node, "modules")
        if node_modules is None:
            return []
        for module in node_modules:
            if os.path.exists(root + "/" + module.text + "/pom.xml"):
                all_module_poms.append(root + "/" + module.text + "/pom.xml")
                sub_path = root + "/" + module.text
                all_module_poms.extend(self.get_all_submodules(sub_path))
        return all_module_poms
