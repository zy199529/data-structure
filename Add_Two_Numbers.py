#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-05-31 22:48:33
# @Last Modified by:   zy19950209
# @Last Modified time: 2019-05-31 23:31:07
class ListNode():

    def __init__(self, value):
        self.value = value
        self.next = None
    # 创建列表
def Createlist(n):
        if n <= 0:
            return False
        if n == 1:
            return ListNode(1)
        else:
            root = ListNode(1)
            tmp = root
            for i in range(2, n+1):
                tmp.next = ListNode(i)
                tmp = tmp.next
        return root

def printlist(head):       # 打印链表 （遍历） 
    p=head  
    while p!=None:  
        print(p.value)  
        p=p.next  

def listlen(head):  # 链表长度
        c = 0
        p = head
        while p != None:
            c = c+1
            p = p.next
        return c

def insert(head, n):  # 插入链表
        if n < 1 or n > listlen(head):
            return
        p = head
        for i in range(1, n-1):
            p = p.next
        t = ListNode(value=a)
        t.next = p.next
        p.next = t
        return head

def dellist(head, n):  # 删除链表
        if n < 1 or n > listlen(head):
            return
        elif n is 1:
            head = head.next
        else:
            p = head
            for i in range(1, n-1):
                p = p.next
            q = p.next
            p.next = q.next
        return head


def main():
    print("Create a linklist")
    head = (7)
    printlist(head)
    print()
    print("___________________________")

    n1 = raw_input("Enter the index to insert")
    n1 = int(n1)
    insert(head, n1)
    printlist(head)
    print()
    print("___________________________")

    n2 = raw_input("Enter the index to delete")
    n2 = int(n2)
    dellist(head, n2)
    printlist(head)


if __name__ == '__main__':
    main()   # 主函数调用
