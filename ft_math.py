class ft_math:
    def __init__(self):
        self.weight = float(0)
        self.power = int(0)
        self.dic = {}
        self.tab = []
    def split_equation(self,data,part):


    def extract_equation(self,data):
            data = data.replace(" ","").replace("\t","").replace("\n","").replace("+"," +").replace("-"," -").replace("="," = ")
            data = data.split("=")
            i = 0
            while i < len(data):
                data[i] = data[i].strip()
                i+=1
            return data
    def reduced_from(lis):

