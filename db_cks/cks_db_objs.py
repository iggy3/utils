import re

def ir_chk_statement(l_statement):

# lets get rid of all the comments in the file
    q = re.sub(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/", "", l_statement)
    # the entire line
    lines = [line for line in q.splitlines() if not re.match("^\s*(--|#)", line)]
    # end of line
    q = " ".join([re.split("--|#", line)[0] for line in lines])
    # split on semic space and parens
    tokens = re.split(r"[\s)(;]+", q)

    # look for something of your choice ans split on it
    # for now we will choose select and join
    # tag this and get next
    result = set()
    get_next = False
    for tok in tokens:
        if get_next:
            if tok.lower() not in ["", "select"]:
                result.add(tok)
            get_next = False
        get_next = tok.lower() in ["from", "join"]

    return result

# a quick test

my_string = 'SELECT * FROM ir_tab a join ir_tab2 b on a.id = b.id;'
print ir_chk_statement(my_string)

#l_obj_t1 = 'SELECT col1, col2, col3 FROM tab1'
#with open('sel_ins_Yellow_Coupon_Printing_Scoring_Code.sh','r') as fd:
#    if 'select' in fd:
#        print ir_chk_statement(my_string)
#    else:
#        print "No tables found"

