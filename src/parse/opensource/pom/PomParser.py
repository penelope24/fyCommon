import re
import os
import xml.etree.ElementTree as ET


class PomParser:

    def __init__(self, pom_file):
        self.M2_reops = "/home/qwe/.m2/repository"
        self.pom_file = pom_file
        self.tree = ET.parse(self.pom_file)
        self.root_node = ET.parse(self.pom_file).getroot()
        f = re.findall("{.*}", self.root_node.tag)
        if re.findall("{.*}", self.root_node.tag) != []:
            self.namespace = True
            self.url = re.findall("{.*}", self.root_node.tag)[0].strip("{}")
            self.ns = {"d": self.url}
        else:
            self.namespace = False
            self.url = None
            self.ns = None

    def find_node(self, node, property):
        """
        note that this function return node object, to get test value, use object.text.
        :param node:
        :param property:
        :return:
        """
        if self.ns:
            r = node.find("d:"+property, self.ns)
            return r
        else:
            r = node.find(property)
            return r

    # def find_all(self, node, property):
    #     if self.ns:
    #         r = node.findall("d:"+property, self.ns)
    #         return r
    #     else:
    #         r = node.findall(property)
    #         return r

    def is_jar_pom(self):
        packaging = self.find_node(self.root_node, "packaging")
        if packaging is None:
            return True
        elif packaging.text == "jar" or packaging.text == "bundle":
            return True
        else:
            return False

    def get_artifact_id(self):
        return self.find_node(self.root_node, "artifactId").text

    def get_group_id(self):
        if self.find_node(self.root_node, "groupId") is not None:
            group_id = self.find_node(self.root_node, "groupId").text
        elif self.find_node(self.root_node, "parent") is not None:
            parent = self.find_node(self.root_node, "parent")
            group_id = self.find_node(parent, "groupId").text
        else:
            group_id = None
        return group_id

    def get_version(self):
        if self.find_node(self.root_node, "version") is not None:
            version = self.find_node(self.root_node, "version").text
        elif self.find_node(self.root_node, "parent") is not None:
            parent = self.find_node(self.root_node, "parent")
            version = self.find_node(parent, "version").text
        else:
            version = None
        return version

    def get_jar_name(self):
        # if can find in root
        artifact_id = self.find_node(self.root_node, "artifactId").text
        if self.find_node(self.root_node, "version") is not None:
            version =self.find_node(self.root_node, "version").text
            return artifact_id + "-" + version + ".jar"
        # cannot find in root, maybe in parent node
        elif self.find_node(self.root_node, "parent") is not None:
            parent = self.find_node(self.root_node, "parent")
            version = self.find_node(parent, "version").text
            return artifact_id + "-" + version + ".jar"
        else:
            return artifact_id + ".jar"


