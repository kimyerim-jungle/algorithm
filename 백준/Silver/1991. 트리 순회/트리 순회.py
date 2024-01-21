import sys

num = int(input())
graph = dict()

for _ in range(num):
    parent, child_left, child_right = sys.stdin.readline().split()
    
    graph[parent] = child_left, child_right
    
def print_subtree_in(node):
    if node != '.':
        print_subtree_in(graph[node][0])
        print(node, end="")
        print_subtree_in(graph[node][1])

def print_subtree_pre(node):
    if node != '.':
        print(node, end="")
        print_subtree_pre(graph[node][0])
        print_subtree_pre(graph[node][1])

def print_subtree_post(node):
    if node != '.':
        print_subtree_post(graph[node][0])
        print_subtree_post(graph[node][1])
        print(node, end="")
    
print_subtree_pre('A')
print()
print_subtree_in('A')
print()
print_subtree_post("A")
       