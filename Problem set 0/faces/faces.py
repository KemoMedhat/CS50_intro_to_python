def convert(txt):
    if(":)" in txt or ":(" in txt):
        o = txt.replace(":)","🙂")
        r = o.replace(":(","🙁")
    print(r)
def main():
    return convert(input())
main()