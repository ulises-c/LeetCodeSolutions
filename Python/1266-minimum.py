# https://leetcode.com/problems/minimum-time-visiting-all-points/submissions/

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        moves = 0
        print("moves:", moves)
        for i in range(len(points)):
                j = i-1
                Xi = points[j][0]
                Yi = points[j][1]
                print("Xi:", Xi, ", Yi:", Yi)
                
                Xf = points[i][0]
                Yf = points[i][1]
                print("Xf:", Xf, ", Yf:", Yf)
                
                Xcur = Xi
                Ycur = Yi
                
                while(Xcur != Xf and Ycur != Yf):
                    if(Xf < Xcur and Yf < Ycur):
                        Ycur -= 1
                        Xcur -= 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print("moves:", moves)
                    elif(Xf == Xcur and Yf < Ycur):
                        Ycur -= 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves -= 1
                        print("moves:", moves)
                    elif(Xf < Xcur and Yf != Ycur):
                        Xcur -= 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print(moves)
                    elif(Xf > Xcur and Yf > Ycur):
                        Ycur += 1
                        Xcur += 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print("moves:", moves)
                    elif(Xf == Xcur and Yf > Ycur):
                        Ycur += 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print("moves:", moves)
                    elif(Xf > Xcur and Yf != Ycur):
                        Xcur += 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print(moves)
                    elif(Xf > Xcur and Yf < Ycur):
                        Ycur -= 1
                        Xcur += 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print("moves:", moves)
                    elif(Xf < Xcur and Yf > Ycur):
                        Ycur += 1
                        Xcur -= 1
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        moves += 1
                        print("moves:", moves)

                    else:
                        print("Xcur:", Xcur, ", Ycur:", Ycur)
                        print("error")
                        print("moves:", moves)
                        
        print("moves:", moves)
        return(moves)