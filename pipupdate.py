import sh
from termcolor import colored
import argparse

def pipupdate(ver, path, show_info):
    command = sh.Command("{0}pip{1}".format(path, ver))
    i = 0
    for package in command("list", "-o",_iter=True):
        pack = package.split('(')[0]
        if len(pack) <= 20:
            print(colored('{0}. Update {1}'.format(i+1, pack), 'green'))
            i += 1
            if show_info:
                print(sh.Command("{0}pip{1}".format(path, ver))("install", "--upgrade",  pack))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', nargs='?', help='Path to pip', default='/usr/bin/')
    parser.add_argument('--ver', nargs='?', help='Version of pip (2,3,3.3...)', default='3.5')
    parser.add_argument('--show-info', help='Show installation information', action='store_true')
    args = parser.parse_args()
    pipupdate(args.ver, args.path, args.show_info)
