# -*- coding:UTF-8 -*-
import os
import xml.dom.minidom


class ReadXML(object):
    def dir_base(self, filename, filePath="data"):
        current_dir = os.path.dirname(__file__)  # 当前文件所在路径，
        # 当前所在路径的的一上级路径，就是工程目录
        prject_dir = os.path.dirname(current_dir)
        return(os.path.join(prject_dir, filePath, filename))

    @classmethod
    def dir_base_cls(cls, filename, filePath="data"):
        current_dir = os.path.dirname(__file__)  # 当前文件所在路径，
        # 当前所在路径的的一上级路径，就是工程目录
        prject_dir = os.path.dirname(current_dir)
        return(os.path.join(prject_dir, filePath, filename))

    def getXMLData(self, value):
        """获取xml文件单节点value中的数据"""
        dom = xml.dom.minidom.parse(self.dir_base("data.xml"))
        # db = dom.documentElement
        db = dom.getElementsByTagName(value)
        name = db[0]
        return name.firstChild.data

    @classmethod
    def getXMLDataCls(cls, value):
        """获取xml文件单节点value中的数据"""
        dom = xml.dom.minidom.parse(cls.dir_base_cls("data.xml"))
        # db = dom.documentElement
        db = dom.getElementsByTagName(value)
        name = db[0]
        return name.firstChild.data

    def getXMLValue(self, parent, child):
        """获取xml文件parent节点中child属性的值"""
        dom = xml.dom.minidom.parse(self.dir_base("data1111.xml"))
        db = dom.getElementsByTagName(parent)
        name = db[0]
        return name.getAttribute(child)

# 用于调试
if __name__ == '__main__':
    rx = ReadXML()
    rx.getXMLData("username")
    print(rx.getXMLValue("loginErrorMsg", "msg1"))