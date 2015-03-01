#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import quadtree.qt


class TestFunctions(unittest.TestCase):
    def test_qt(self):
        tree = quadtree.qt.Tree()
        r = tree.root
        self.assertEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(tree.status_for_path([0]),quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(tree.status_for_path([0,1,2]),quadtree.qt.NodeStatus.GRAY)

    def test_qt_0(self):
        tree = quadtree.qt.Tree()
        tree.add_terminal([0,1,2,3],True,'terminal0123')

        r = tree.root
        self.assertNotEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
                
        self.assertEqual(r.children[0].children[0],None)
        self.assertNotEqual(r.children[0].children[1],None)
        self.assertEqual(r.children[0].children[2],None)
        self.assertEqual(r.children[0].children[3],None)
        self.assertEqual(r.children[0].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].parent,r)
                
        self.assertEqual(r.children[0].children[1].children[0],None)
        self.assertEqual(r.children[0].children[1].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2],None)
        self.assertEqual(r.children[0].children[1].children[3],None)
        self.assertEqual(r.children[0].children[1].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].parent,r.children[0])
                
        self.assertEqual(r.children[0].children[1].children[2].children[0],None)
        self.assertEqual(r.children[0].children[1].children[2].children[1],None)
        self.assertEqual(r.children[0].children[1].children[2].children[2],None)
        self.assertNotEqual(r.children[0].children[1].children[2].children[3],None)
        self.assertEqual(r.children[0].children[1].children[2].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].children[2].parent,r.children[0].children[1])
                
        self.assertEqual(r.children[0].children[1].children[2].children[3].status,quadtree.qt.NodeStatus.EXISTING_TERMINAL)
        self.assertEqual(r.children[0].children[1].children[2].children[3].parent,r.children[0].children[1].children[2])
                
        self.assertEqual(tree.status_for_path([0,1,2,3]),quadtree.qt.NodeStatus.EXISTING_TERMINAL)
        self.assertEqual(tree.status_for_path([0,1,2,3,2,1]),quadtree.qt.NodeStatus.EXISTING_TERMINAL)
        self.assertEqual(tree.status_for_path([0,1,2,2]),quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(tree.status_for_path([0,1,2]),quadtree.qt.NodeStatus.GRAY)

    def test_qt_1(self):
        tree = quadtree.qt.Tree()
        tree.add_terminal([0,1,2,3],True,'terminal0123')
        tree.add_terminal([0,1,2,2],True,'terminal0122')

        r = tree.root
        self.assertNotEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
                
        self.assertEqual(r.children[0].children[0],None)
        self.assertNotEqual(r.children[0].children[1],None)
        self.assertEqual(r.children[0].children[2],None)
        self.assertEqual(r.children[0].children[3],None)
        self.assertEqual(r.children[0].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].parent,r)
                
        self.assertEqual(r.children[0].children[1].children[0],None)
        self.assertEqual(r.children[0].children[1].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2],None)
        self.assertEqual(r.children[0].children[1].children[3],None)
        self.assertEqual(r.children[0].children[1].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].parent,r.children[0])
                
        self.assertEqual(r.children[0].children[1].children[2].children[0],None)
        self.assertEqual(r.children[0].children[1].children[2].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2].children[2],None)
        self.assertNotEqual(r.children[0].children[1].children[2].children[3],None)
        self.assertEqual(r.children[0].children[1].children[2].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].children[2].parent,r.children[0].children[1])
                
        self.assertEqual(r.children[0].children[1].children[2].children[2].status,quadtree.qt.NodeStatus.EXISTING_TERMINAL)
        self.assertEqual(r.children[0].children[1].children[2].children[2].parent,r.children[0].children[1].children[2])
        self.assertEqual(r.children[0].children[1].children[2].children[3].status,quadtree.qt.NodeStatus.EXISTING_TERMINAL)
        self.assertEqual(r.children[0].children[1].children[2].children[3].parent,r.children[0].children[1].children[2])

    def test_qt_2(self):
        tree = quadtree.qt.Tree()
        tree.add_terminal([0,1,2,3],True,'terminal0123')
        tree.add_terminal([0,1,2,2],True,'terminal0122')
        tree.add_terminal([0,1,2,0],True,'terminal0120')
        tree.add_terminal([0,1,2,1],True,'terminal0121')

        r = tree.root
        self.assertNotEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
                
        self.assertEqual(r.children[0].children[0],None)
        self.assertNotEqual(r.children[0].children[1],None)
        self.assertEqual(r.children[0].children[2],None)
        self.assertEqual(r.children[0].children[3],None)
        self.assertEqual(r.children[0].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].parent,r)
                
        self.assertEqual(r.children[0].children[1].children[0],None)
        self.assertEqual(r.children[0].children[1].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2],None)
        self.assertEqual(r.children[0].children[1].children[3],None)
        self.assertEqual(r.children[0].children[1].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].parent,r.children[0])

        self.assertEqual(r.children[0].children[1].children[2].status,quadtree.qt.NodeStatus.EXISTING_TERMINAL)

    def test_qt_3(self):
        tree = quadtree.qt.Tree()
        tree.add_terminal([0,1,2,3],False,'terminal0123')
        tree.add_terminal([0,1,2,2],False,'terminal0122')
        tree.add_terminal([0,1,2,0],False,'terminal0120')
        tree.add_terminal([0,1,2,1],False,'terminal0121')

        r = tree.root
        self.assertNotEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
                
        self.assertEqual(r.children[0].children[0],None)
        self.assertNotEqual(r.children[0].children[1],None)
        self.assertEqual(r.children[0].children[2],None)
        self.assertEqual(r.children[0].children[3],None)
        self.assertEqual(r.children[0].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].parent,r)
                
        self.assertEqual(r.children[0].children[1].children[0],None)
        self.assertEqual(r.children[0].children[1].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2],None)
        self.assertEqual(r.children[0].children[1].children[3],None)
        self.assertEqual(r.children[0].children[1].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].parent,r.children[0])

        self.assertEqual(r.children[0].children[1].children[2].status,quadtree.qt.NodeStatus.EMPTY_TERMINAL)

    def test_qt_4(self):
        tree = quadtree.qt.Tree()
        tree.add_terminal([0,1,2,3],False,'terminal0123')
        tree.add_terminal([0,1,2,2],True,'terminal0122')
        tree.add_terminal([0,1,2,0],True,'terminal0120')
        tree.add_terminal([0,1,2,1],False,'terminal0121')

        r = tree.root
        self.assertNotEqual(r.children[0],None)
        self.assertEqual(r.children[1],None)
        self.assertEqual(r.children[2],None)
        self.assertEqual(r.children[3],None)
        self.assertEqual(r.status,quadtree.qt.NodeStatus.GRAY)
                
        self.assertEqual(r.children[0].children[0],None)
        self.assertNotEqual(r.children[0].children[1],None)
        self.assertEqual(r.children[0].children[2],None)
        self.assertEqual(r.children[0].children[3],None)
        self.assertEqual(r.children[0].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].parent,r)
                
        self.assertEqual(r.children[0].children[1].children[0],None)
        self.assertEqual(r.children[0].children[1].children[1],None)
        self.assertNotEqual(r.children[0].children[1].children[2],None)
        self.assertEqual(r.children[0].children[1].children[3],None)
        self.assertEqual(r.children[0].children[1].status,quadtree.qt.NodeStatus.GRAY)
        self.assertEqual(r.children[0].children[1].parent,r.children[0])

        self.assertEqual(r.children[0].children[1].children[2].status,quadtree.qt.NodeStatus.SURELY_MIXED)

if __name__ == '__main__':
    unittest.main()
