import unittest
from src.parse.opensource.pom.PomParser import PomParser
import xml.etree.ElementTree as ET


class TestPomParser(unittest.TestCase):

    """unittest way to override __init__()"""
    def setUp(self):
        # a normal root pom.xml
        self.path1 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/spring-projects-spring-data-mongodb/" \
                     "spring-data-mongodb/pom.xml"
        # a pom.xml which dont have namespaces
        self.path2 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/svn2github-aTunes/aTunes/plugins/" \
                     "instantmessaging/pom.xml"

        # a root pom but its <version> is in <parent>
        self.path3 = "/home/qwe/disk1/zfy_lab/bigcode_data/projects/zkoss-zk/zk/zhtml/pom.xml"

        # a project that needs to modify its compiler plugin slash
        self.path4 = "/home/qwe/disk1/zfy_lab/bigcode_data/data2/1181888200/activeMQ/lwl-activemq/pom.xml"

    def test_init(self):
        parser = PomParser(self.path2)

    def test_find_property(self):
        parser = PomParser(self.path1)
        self.assertEqual(parser.find_node(parser.root_node, "packaging").text, "pom")
        self.assertEqual(parser.find_node(parser.root_node, "url").text, "https://projects.spring.io/spring-data-mongodb")

        parser2 = PomParser(self.path2)
        self.assertEqual(parser2.find_node(parser2.root_node, "artifactId").text, "instantmessaging")

    def test_is_jar(self):
        parser = PomParser("/home/qwe/disk2/85_3000/repository/orbisgis@orbisgis/orbisgis-commons/pom.xml")

    def test_get_install_name(self):
        parser3 = PomParser(self.path3)
        self.assertEqual(parser3.get_jar_name(), "zhtml-9.5.0-SNAPSHOT.jar")

    def test_get_artifact_id(self):
        parser1 = PomParser(self.path1)
        parser2 = PomParser(self.path2)
        parser3 = PomParser(self.path3)
        self.assertEqual(parser1.get_artifact_id(), "spring-data-mongodb-parent")
        self.assertEqual(parser2.get_artifact_id(), "instantmessaging")
        self.assertEqual(parser3.get_artifact_id(), "org.zkoss.zk")

    def test_get_group_id(self):
        parser1 = PomParser(self.path1)
        parser2 = PomParser(self.path2)
        parser3 = PomParser(self.path3)
        self.assertEqual(parser1.get_artifact_id(), "org.springframework.data")
        self.assertEqual(parser2.get_artifact_id(), "net.sourceforge.atunes.plugins")
        self.assertEqual(parser3.get_artifact_id(), "zhtml")

    def test_get_version(self):
        parser1 = PomParser(self.path1)
        parser2 = PomParser(self.path2)
        parser3 = PomParser(self.path3)
        self.assertEqual(parser1.get_version(), "3.1.0-SNAPSHOT")
        self.assertEqual(parser2.get_version(), "1.0.1")
        self.assertEqual(parser3.get_version(), "9.5.0-SNAPSHOT")


if __name__ == "__main__":
    unittest.main()
