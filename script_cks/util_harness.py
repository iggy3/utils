#!/usr/bin/python
"""Return an integer based on file contents."""
#####################################################
# Script : Utility Harness                          #
# desc: This is an entry point to vaidate scripts.  #
#       Associates an integer for script contents   #
#                                                   #
#####################################################
import re, string

def ir_container(ir_pods):
    p = re.compile(
        string.join(map(lambda x: "("+x+")", ir_pods), "|")
        )
    def ir_munge(v, m=p.search, r=range(0,len(ir_pods))):
        try:
            regs = m(v).regs
        except AttributeError:
            return -1 #when not receiving a match give us a negative 1
        else:
            for i in r:
                if regs[i+1] != (-1, -1):
                    return i
    return ir_munge

# lets provide the patterns we want to check                #
# Create function to hand off the following to ir_container #

ir_pods = [
    r"bteq << !", # bteq is 3
    r"eoj", # eoj is 4

]

p = ir_container(ir_pods)

# quick tests
print p("bteq << !")
print p("eoj")


# Create function to hand off the following to call
with open('afile1.txt','r') as fd:
            if 'bteq << !' in fd.read():
                print p("bteq << !")
            else:
                print "login not found"
                # add read file out to tmp
                # prepend hdr


with open('afile1.txt','r') as fd:
            if 'eoj' in fd.read():
                print p("eoj")
            else:
                print "logout not found"
                # add read file out to tmp
                # prepend footer

