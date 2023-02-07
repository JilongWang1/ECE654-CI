import os
import ast_walk


class Test:
    def TestAst(self):
        for project in os.listdir('.//test_cases'):
            for root, dirs, files in os.walk('.//test_cases//' + project):
                for file in files:
                    if '.py' in file:
                        name_13, depth = ast_walk.ast_walk(root + '//' + file)

                        assert not name_13
                        assert depth <= 4

a = Test()
a.TestAst()
