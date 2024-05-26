import sys
import os
def wannaknow():
    print('wannaknow')
def we_are_frozen():
    return hasattr(sys, "frozen")
def module_path():
    print('encode')
    encoding = sys.getfilesystemencoding()
    print(encoding)
    if we_are_frozen():
        print('in if')
        # python2
        return os.path.dirname(unicode(sys.executable, encoding))
    # python2
    return os.path.dirname(unicode(__file__, encoding))
