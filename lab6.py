####################################################################################
# Name: Nicholas Buckley
# Pledge: I pledge my honor that I have abided by the Stevnes Honor System
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#
# Note: Using anything other than recursion will result in a penalty
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################

'''
Other Test Case
(hello, __hello)
('!_hello', 'ahello')
'''

def LLCS(S1, S2):
    count = 0
    use_it = 0
    lose_it = 0
        
    if S1 == '' or S2 == '':
        count = 0
    else:
        if S1[0] == S2[0]:
            count = 1 + LLCS(S1[1:],S2[1:])
            
        else:
            use_it = LLCS(S1,S2[1:])
            lose_it = LLCS(S1[1:],S2)

            count = max(use_it, lose_it)
       
    return count

    

    

    
##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    string = ""
    use_it = ""
    lose_it = ""
        
    if S1 == '' or S2 == '':
        string = ''
    else:
        if S1[0] == S2[0]:
            string = S1[0] + LCS(S1[1:],S2[1:])
            
        else:
            use_it = LCS(S1,S2[1:])
            lose_it = LCS(S1[1:],S2)

            if(len(use_it) > len(lose_it)):
                string = use_it
            else:
                string = lose_it
       
    return string
