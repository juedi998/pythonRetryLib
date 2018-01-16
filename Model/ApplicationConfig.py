import json,os
class ApplicationConfig():
    path = r'Links.json'
    def WriteFile(self,Centens):
        JsonFexd = json.dumps(Centens,ensure_ascii=False)
        with open(self.path,'w')as df:
            df.write(JsonFexd)

    def ReadFile(self):
        JsonFexd = None
        with open(self.path,'r')as df:
            JsonFexd = df.read()
        JsonFexds = json.loads(JsonFexd)
        return JsonFexds

    def IsEist(self):
        if(os.path.exists(self.path)):
            return True
        else:
            return False

