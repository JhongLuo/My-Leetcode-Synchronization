class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        from collections import defaultdict
        creator2views = defaultdict(int)
        creator2best_video = dict()
        most_views = 0
        for i in range(n):
            creator = creators[i]
            creator2views[creator] += views[i]
            most_views = max(most_views, creator2views[creator])
            if (creator not in creator2best_video) or \
                (views[i] > views[creator2best_video[creator]]) or \
                (views[i] == views[creator2best_video[creator]] and
                    ids[i] < ids[creator2best_video[creator]]):
                creator2best_video[creator] = i
        res = list()
        # print(creator2best_video, creator2views)
        for creator, views in creator2views.items():
            if views == most_views:
                res.append([creator, ids[creator2best_video[creator]]])
        return res
