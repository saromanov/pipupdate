import sh
from termcolor import colored
import argparse

def pipupdate(ver, path, show_info=False, exceptv=[]):
    '''
    Args:
      ver - version of python
      path - path to pip
      show_info - Show update information during work
      execeptv - update all packages except from this list

    Example:
      pipupdate('3.4', '/usr/local/bin/pip3.4)
    '''
    command = sh.Command("{0}pip{1}".format(path, ver))
    i = 0
    for package in command("list", "-o",_iter=True):
        pack = package.split('(')[0]
        if len(pack) <= 20 and pack not in exceptv:
            msg = '{0}. Update {1}'.format(i+1, pack)
            print(colored(msg, 'green'))
            i += 1
            if show_info:
                print(sh.Command("{0}pip{1}".format(path, ver))("install", "--upgrade",  pack))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', nargs='?', help='Path to pip', default='/usr/bin/')
    parser.add_argument('--ver', nargs='?', help='Version of pip (2,3,3.3...)', default='3.5')
    parser.add_argument('--show-info', help='Show installation information', action='store_true')
    parser.add_argument('--without', nargs='+', help='update except this packages', default=[])
    args = parser.parse_args()
    pipupdate(args.ver, args.path, show_info=args.show_info, execptv=args.without)
