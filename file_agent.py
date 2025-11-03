from agent import Agent
class File_Agent(Agent):
    def __init__(self, code_name: str, clearance_level: int,property_region:str):
        super().__init__(code_name,clearance_level)
        self.property_region=property_region
    def report(self):
        print(f" Agent:{self.code_name} reporting. clearing level: {self._clearance_level},property region:{self.property_region}")

