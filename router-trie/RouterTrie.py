class RouteTrieNode:
    def __init__(self):
        self.routes = {}
        self.handler = None

    def insert(self, route):
        if route not in self.routes:
            self.routes[route] = RouteTrieNode()


class RouteTrie:
    def __init__(self, root_handler):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, route, handler, current_node=None):
        if current_node is None:
            current_node = self.root

        if len(route) == 0:
            current_node.handler = handler

        elif len(route) == 1:
            current_node.insert(route[0])
            current_node.routes[route[0]].handler = handler

        else:
            current_node.insert(route[0])
            self.insert(route[1:], handler, current_node.routes[route[0]])

    def find(self, route, current_node=None):
        if current_node is None:
            current_node = self.root

        if len(route) == 0:
            return current_node.handler

        else:

            if route[0] in current_node.routes:
                return self.find(route[1:], current_node.routes[route[0]])

            else:
                return None


def split_path(path):
    splitted_path = path.split('/')[1:]

    if len(splitted_path) == 0:
        return []

    if splitted_path[-1] == "":
        return splitted_path[:-1]

    return splitted_path


class Router:
    def __init__(self, root_handler, not_found_handler):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        self.route_trie.insert(split_path(path), handler)

    def lookup(self, path):
        handler = self.route_trie.find(split_path(path))
        return handler if handler else self.not_found_handler

