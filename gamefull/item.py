
class Item:
    def __init__(self, name, durabillity = 0, stat = None,  unbreak = False):
        self.name = name
        self.stat = stat
        self.durabillity = durabillity
        self.unbreak = unbreak

    def use(self):
       if self.durabillity <= 0:
           return None
       if not self.unbreak:
            self.durabillity -= 1
       return self.stat

    def is_broken(self):
        return self.durabillity <= 0

class weapone:
        def __init__(self, name = "", durabillity = 0, stat = None,  unbreak = False, DAMAGE = 0):
           Item.__init__(self, name,durabillity,DAMAGE)
           self.durabillity = durabillity

        def set_procent_DM(self):
            if (self.durabillity <= (self.durabillity/2)):
                self.DAMAGE = self.DAMAGE/2
                print(self.DAMAGE)
            if (self.durabillity <= self.durabillity/5):
                self.DAMAGE = self.DAMAGE/5
                print(self.DAMAGE)







