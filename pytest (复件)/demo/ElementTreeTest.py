__author__ = 'gengjie'
from xml.etree import ElementTree as ET


def walkTree(node):
    print node.tag, ':', node.text
    if node.tag == 'author':
        node.text = 'gengjie'
    if node.attrib:
        print "\t", node.attrib
    childlist = node.getchildren()
    if childlist is not None:
        for cnode in childlist:
            walkTree(cnode)


filename = "./ProjectTest.xml"
tree = ET.parse(filename)
root = tree.getroot()
# print repr(root), root.tag
walkTree(root)
tree.write(filename)