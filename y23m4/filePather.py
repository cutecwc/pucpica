# TODO: file to rematch.
import re


# TODO: to split the target. the answer has two: None or <re.Match object; span=(12, 32), match='user-places.xbel.bak'>
def func_LineSplitByRe(anylines, nameextra):
    # re test: \b[a-z0-9A-Z.=\-_]*\b
    strs = re.search(nameextra, anylines)
    if strs is not None:
        print(strs.group())
    else:
        print("")


# TODO: single file by walker.
# func_ReviseLinkByWalker("file://filesystem/path", r"regex description")
def func_ReviseLinkByWalker(filepath, nameextra, listmatched, substr="nothing needed"):
    f1 = open(filepath, 'r')
    freadline = f1.readlines()
    f1.close()
    # f2 = open(filepath, "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        # a = re.sub(nameextra, substr, eachline)
        # f2.writelines(a)
        strs = re.search(nameextra, eachline)
        if strs is not None:
            listmatched.append(strs.group())
    return listmatched
    # f2.close()

def func_flat(filepath, nameextra, listold, substr="nothing needed"):
    f1 = open(filepath, 'r')
    freadline = f1.readlines()
    f1.close()
    f2 = open("./new.result", "w+")
    for eachline in freadline:
        # set match and what to replace!, you need to change here?
        # a = re.sub(nameextra, substr, eachline)
        # f2.writelines(a)
        strs = re.search(nameextra, eachline)
        if strs is not None:
            if strs.group() in listold:
                f2.writelines("(   )" + eachline)
            else:
                f2.writelines("(+++)" + eachline)
    f2.close()

if __name__ == '__main__':
    print("hello world!")
    nameextra = r"\b[a-z0-9A-Z.=\-_]+\b"
    listsource = []
    listsource = func_ReviseLinkByWalker("./treeold.txt", nameextra, listsource)
    func_flat("./tree.txt", nameextra, listsource)
