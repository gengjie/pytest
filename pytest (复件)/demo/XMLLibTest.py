# -*-coding=utf-8-*-
import libxml2


def get_xpath_1():
    doc = libxml2.parseFile("./ProjectTest.xml")  #data.xml文件结构与上述的input_xml_string相同
    for node in doc.xpathEval("//item/data[@version = '1.0']"):
        print (node, node.name, (node.properties.name, node.properties.content))
    doc.freeDoc()


if __name__ == "__main__":
    get_xpath_1()

    doc = libxml2.parseFile("./ProjectTest.xml")
    root = doc.children
    # print root
    #iterate over children of verse
    child = root.children
    while child is not None:
        print repr(child), child.type
        if child.type == 'text':
            print '--->', child.getContent()
        elif child.type == "element":
            # print "\tAn element with ", child.lsCountNode(), "child(ren)"
            # print "\tAnd content", repr(child.content)
            print child.content
        child = child.next

        # doc = minidom.parse("./ProjectTest.xml")
        # root = doc.documentElement


