# number of scores
def main():
    d = {1:1, 2:2, 3:3}
    # print(scores(6, d))
    scores(6, d)
    
def scores(score, dict):
    if score in dict.keys():
        return dict[score]
    else:
        ans = scores(score-1, dict) + scores(score-2, dict) + scores(score-3, dict)
        dict[score] = ans
        return ans

# main()    