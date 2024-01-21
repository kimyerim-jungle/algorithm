import sys

num = int(input())
graph = {i:[] for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

for _ in range(num):
    parent, child_left, child_right = sys.stdin.readline().split()
    graph[parent] += [child_left, child_right]

def preorder(graph, root):
    stack = [root]
    result = ''
    
    while stack:
        node = stack.pop()
        result += node
        
        if graph[node][1] != '.':
            stack.append(graph[node][1])
        
        if graph[node][0] != '.':
            stack.append(graph[node][0])
            
    return result

def inorder(graph, root):
    stack = [root]
    result = ''
    
    while stack:
        if graph[stack[-1]][0] != '.' and graph[stack[-1]][0] not in result:
            stack.append(graph[stack[-1]][0])
            
        elif stack[-1] in result:
            stack.append(graph[stack[-1]][1])
            
        else: 
            node = stack.pop()
            result += node
            if graph[node][1] != '.':
                stack.append(graph[node][1])
    return result

def postorder(graph, root):
    stack = [root]
    result = ''
    
    while stack:
        if graph[stack[-1]][0] != '.' and graph[stack[-1]][0] not in result:
            stack.append(graph[stack[-1]][0])
            
        elif graph[stack[-1]][1] == '.' or graph[stack[-1]][1] in result:
            result += stack.pop()
        
        else:
            stack.append(graph[stack[-1]][1])
    return result

print(preorder(graph, "A"))
print(inorder(graph, "A"))
print(postorder(graph, "A"))
    