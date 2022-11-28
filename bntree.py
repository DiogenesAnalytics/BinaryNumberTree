import itertools
from treelib import Tree


class BinaryNumberTree(Tree):
    """Generate binary tree of all binary numbers of a certain bit-length."""
    def __init__(self, depth: int) -> None:
        # call super class constructor
        super().__init__()

        # create root
        self.create_node("{}", "")

        # loop over tree depth
        for level in range(depth):
            # get parent duplicate pairs
            parent_duplicates = (
                ''.join(parent) for parent in itertools.product('01', repeat=level) for _ in (0, 1)
            )

            # get children nodes
            children = (''.join(combo) for combo in itertools.product('01', repeat=level+1))

            # populate tree
            for value, (parent, child) in enumerate(zip(parent_duplicates, children)):
                # add new node
                self.create_node(value%2, child, parent=parent)


# executable
if __name__ == '__main__':
    # get argparse
    import argparse

    # declare purpose
    parser = argparse.ArgumentParser(
        description=BinaryNumberTree.__doc__,
        prog='bntree'
    )

    # declare cli args
    parser.add_argument(
        'depth',
        metavar='depth',
        type=int,
        help='depth of the binary tree or bit-length of binary numbers'
    )

    # now get args
    args = parser.parse_args()

    # create bn tree
    bntree = BinaryNumberTree(args.depth)

    # now show
    bntree.show()

    # now print total combinations
    print(f'Total combinations: {2**(int(args.depth))}')
