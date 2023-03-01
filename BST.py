# created a class Node to store data at each node
import logging

logging.basicConfig(filename="log.txt", format="%(levelname)s : %(asctime)s : %(message)s", level=logging.NOTSET,
                    filemode="w")


class Node:
    left = None
    right = None
    val = 0

    def __init__(self, val):
        self.val = val


class BST:
    found = False

    def __init__(self):
        self.root = None

    def helper(self, root, val):
        if root is None:
            msg = "adding {} to BST".format(val)
            logging.debug(msg)
            return Node(val)
        if root.val == val:
            return root
        elif root.val < val:
            root.right = self.helper(root.right, val)
        elif root.val > val:
            root.left = self.helper(root.left, val)
        return root

    def insert(self, val):
        self.root = self.helper(self.root, val)

    def BFS(self, key=-1):
        logging.info("entered BFS function")
        bfs = []
        bfs.append([self.root, 0])
        flag = False
        level = 0
        output = []
        newOut = []
        while len(bfs) != 0:
            curr = bfs[0]
            msg = "curretly at node {}".format(curr[0].val)
            logging.debug(msg)
            bfs.pop(0)
            # print("level: {} curr.level : {}".format(level, curr[1]))
            if curr[0].val == key:
                flag = True
            if level < curr[1]:
                # print()
                output.append(newOut.copy())
                newOut.clear()
                level = level + 1
            # print("{} ".format(curr[0].val), end="")
            newOut.append(curr[0].val)
            if curr[0].left != None:
                bfs.append([curr[0].left, curr[1] + 1])
            if curr[0].right != None:
                bfs.append([curr[0].right, curr[1] + 1])
        output.append(newOut.copy())
        state = ""
        if flag:
            logging.debug("key value = {} found".format(key))
            state = "YES"
        else:
            logging.debug("key value = {} not found".format(key))
            state = "NO"
        logging.info("succesfully executed and exiting BFS function")
        return output, state

    def DFSHelper(self, root, ans, key=-1):
        # we are writing for inorder
        if root is None:
            return
        if root.val == key:
            self.found = True
        self.DFSHelper(root.left, ans, key)
        msg = "curretly at node {}".format(root.val)
        logging.debug(msg)
        # print(root.val, end=" ")
        ans.append(root.val)
        self.DFSHelper(root.right, ans, key)

    def DFS(self, key=-1):
        logging.info("Entering DFS function")
        ans = []
        self.DFSHelper(self.root, ans, key)
        state = ""
        if self.found:
            logging.debug("key value = {} found".format(key))
            state = "YES"
        else:
            logging.debug("key value = {} not found".format(key))
            state = "NO"
        self.found = False
        logging.info("succesfully executed and exiting DFS function")
        return ans, state