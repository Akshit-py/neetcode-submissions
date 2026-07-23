class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps=sorted(zip(position,speed),reverse=True)
        st=[]
        for i,j in ps:
            t=(target-i)/j
            st.append(t)
            if len(st)>=2 and st[-1]<=st[-2]:
                st.pop()
        return len(st)
            