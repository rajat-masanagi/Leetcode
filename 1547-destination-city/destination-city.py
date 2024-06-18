class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        city=set()
        startcity=set()
        for i in range(len(paths)):
            city.add(paths[i][0])
            city.add(paths[i][1])
            startcity.add(paths[i][0])
        return list(city-startcity)[0]