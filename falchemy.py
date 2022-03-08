def slugify(text):
    title = ""
    for latter in text:
        if latter == " ":
            title += "-"
        elif ord(latter) in list(range(65, 91)) or ord(latter) in list(range(97, 123)):
            title += latter.lower()
    return title


def highlight_word(text, term, tag="font"):
    text = text.replace(term.lower(), f"<{tag} style='background-color:yellow;'>{term.lower()}</{tag}>")
    text = text.replace(term.title(), f"<{tag} style='background-color:yellow;'>{term.title()}</{tag}>")
    text = text.replace(term.upper(), f"<{tag} style='background-color:yellow;'>{term.upper()}</{tag}>")
    return text


def qsort(inlist):
    if inlist == []: 
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater