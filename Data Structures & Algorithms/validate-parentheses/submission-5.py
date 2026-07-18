class Solution:
    def isValid(self, s: str) -> bool:
        l=len(s)
        if l%2==1 or s[0] in (']',')','}'):
            return False
        st=[]
        for i in range(0,l):
            if s[i] in ('{','(','['):
                st.append(s[i])
            elif len(st)==0 and s[i] in ('}',')',']'):
                return False
            elif s[i]==']' and st[-1]!='[':
                return False
            elif s[i]==')' and st[-1]!='(':
                return False
            elif s[i]=='}' and st[-1]!='{':
                return False
            else:
                st.pop()
            print(st)
        print('final: ',st)
        print(len(st))
        if len(st)==0:
            return True
        else:
            return False
        
