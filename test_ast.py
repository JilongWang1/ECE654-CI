import os
import ast_walk


class Test_ast:
    def test_ast(self):
        positive_13 = 0
        negative_13 = 0
        positive_depth = 0
        negative_depth = 0

        for root, dirs, files in os.walk('numpngw'):
            for file in files:
                if file.endswith('.py'):
                    name_13, depth = ast_walk.ast_walk(root + '//' + file)

                    if name_13 == False:
                        positive_13 += 1
                    else:
                        negative_13 += 1

                    if depth > 4:
                        negative_depth += 1
                    else:
                        positive_depth += 1

        print("target\t\tpos_num\t\tneg_num")
        print("length!=13\t" + str(positive_13) + "\t\t" + str(negative_13))
        print("depth<=4\t" + str(positive_depth) + "\t\t" + str(negative_depth))
                        

a = Test_ast()
a.test_ast()
