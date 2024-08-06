class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        if not creators:
            return []
        creatorToViews = {}
        
        creatorsToHighestViewedVideo = {}
        
        for i in range(len(creators)):
            if creators[i] not in creatorToViews:
                creatorToViews[creators[i]] = 0
            creatorToViews[creators[i]] += views[i]
            
            if creators[i] not in creatorsToHighestViewedVideo:
                creatorsToHighestViewedVideo[creators[i]] = (-1, "")
            if (creatorsToHighestViewedVideo[creators[i]][0] < views[i]
               or (creatorsToHighestViewedVideo[creators[i]][0] == views[i] and ids[i] < 
                  creatorsToHighestViewedVideo[creators[i]][1])):
                creatorsToHighestViewedVideo[creators[i]] = (views[i], ids[i])
                
        ans = []
        
        creatorList = []
        
        for key in creatorToViews:
            creatorList.append((creatorToViews[key], key))
            
        creatorList = sorted(creatorList, key=lambda x:x[0], reverse=True)
        
        topViews = creatorList[0][0]
        
        for i in range(len(creatorList)):
            if creatorList[i][0] == topViews:
                ans.append([creatorList[i][1], creatorsToHighestViewedVideo[creatorList[i][1]][1]])
                
        return ans