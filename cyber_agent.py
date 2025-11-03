from agent import Agent

class Cyber_agent(Agent):
    def __init__(self, code_name: str, clearance_level: int,property_specialty:str):
        super().__init__(code_name,clearance_level)
        self.property_specialty=property_specialty
    def report(self):
        print(f" Agent:{self.code_name} reporting. clearing level: {self._clearance_level},property specialty:{self.property_specialty}")
    def list_obj(self,lst:list[Agent]):
        for agent in lst:
            agent.report()



