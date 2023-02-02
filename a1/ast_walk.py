import ast


class Analyzer(ast.NodeVisitor):
    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        max_depth = 0
        name_len13 = False
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, ast.AST):
                        name_len_inv, depth = self.visit(item)
                        max_depth = max(depth, max_depth)
                        name_len13 |= name_len_inv

            elif isinstance(value, ast.AST):
                name_len_inv, depth = self.visit(value)
                max_depth = max(depth, max_depth)
                name_len13 |= name_len_inv

        return name_len13, max_depth

    def visit_Name(self, node):
        if len(node.id) == 13:
            return True, 0

        return False, 0

    def visit_While(self, node):
        name_len13, last_depth = self.generic_visit(node)
        return name_len13, last_depth + 1

    def visit_If(self, node):
        name_len13, last_depth = self.generic_visit(node)
        return name_len13, last_depth + 1

    def visit_For(self, node):
        name_len13, last_depth = self.generic_visit(node)
        return name_len13, last_depth + 1


def ast_walk(path):
    with open(path, 'r') as target:
        tree = ast.parse(target.read())

    ana = Analyzer()
    return ana.visit(tree)
