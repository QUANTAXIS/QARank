from QUANTAXIS.QAARP.QARisk import QA_Risk, QA_Performance
from QUANTAXIS.QAARP.QAAccount import QA_Account

class QA_Rank():
    def __init__(acc:QA_Account):
        self.acc = acc

        self.risk = QA_Risk(acc)
        self.performance = QA_Performance(acc)
        
        print(acc)

    def rank(self):
        pass

    @property
    def message(self):
        return {
            'alpha': self.risk.alpha
        }