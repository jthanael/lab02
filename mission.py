# Thanael Jean Philippe
# MWCC-CIS109
# Mission Briefing

# Agent Name 
agent_name = input("Enter your agent name: ")
agent_age = int(input("Enter your agent age: "))
agent_training_years = int(input("Enter your agent training years: "))
agent_favorite_color = input("Enter your agent favorite color: ")
agent_number_of_gadgets = int(input("Enter your agent number of gadgets: "))
how_many_minutes = int(input("Enter your agent number of minutes in mission completion: "))


# Training Percentage Calculation
training_percentage = (agent_training_years / agent_age) * 100

print(f"Agent {agent_name} is {training_percentage}% trained.")

# Gadget Density Calculation
gadget_density = agent_number_of_gadgets / agent_age

print(f"Agent {agent_name} has a gadget density of {gadget_density:.2f} gadgets per year of age.")


# Mission Seconds Convertion 
mission_seconds = how_many_minutes * 60

print(f"Agent {agent_name} completed the mission in {mission_seconds} seconds.")


# Mission Code
mission_code = f"{agent_name[:3].upper()}{agent_age}{agent_favorite_color}"
print(f"Agent {agent_name}'s mission code is {mission_code}.")




