from agent import Agent
from file_agent import File_Agent
from mission import Mission
from cyber_agent import Cyber_agent

lst=[]
agent_1=Agent("solder in 8200",1)
lst.append(agent_1)
agent_1.report()
agent_property=agent_1.get()
print(agent_property)
print(agent_1.set(agent_property))
Agent.get_total_agents(Agent.total_agents)
file_agent=File_Agent("agent of mossad",2,"tel aviv")
lst.append(file_agent)
file_agent.report()
file_agent_property=file_agent.get()
print(file_agent_property)
print(file_agent.set(file_agent_property))
file_agent.get_total_agents(Agent.total_agents)
mission=Mission("mission 1","aza",agent_1)
mission.assigned(agent_1)
mission.brief()
cyber_agent=Cyber_agent("solder in 8200 cyber",1,"jerusalem")
lst.append(cyber_agent)
cyber_agent.report()
cyber_agent.list_obj(lst)

