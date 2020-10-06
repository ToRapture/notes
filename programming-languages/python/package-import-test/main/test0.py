import sys


def modify_variables_of_module():
    def modify_imported_variables():
        from foo import x
        print('before modified in func modify_imported_variables foo.x is %s' % x)
        x = 'modified in modify_imported_variables'

    def modify_imported_module():
        import foo
        print('before modified in func modify_imported_module foo.x is %s' % foo.x)
        foo.x = 'modified in modify_imported_module'

    def print_imported_variables():
        from foo import x
        print('from foo import x, x is %s' % x)

        import foo
        print('import foo, foo.x is %s' % foo.x)

    def print_from_other_module():
        import bar
        print('bar.variables_of_foo is %s' % bar.variables_of_foo())

    modify_imported_variables()
    print_imported_variables()
    print_from_other_module()

    modify_imported_module()
    print_imported_variables()
    print_from_other_module()


def main():
    print('sys.path from pkg_test is %s' % sys.path)

    modify_variables_of_module()


if __name__ == '__main__':
    main()
