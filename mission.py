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


# Gadget Density Calculation
gadget_density = agent_number_of_gadgets / agent_age



# Mission Seconds Convertion 
mission_seconds = how_many_minutes * 60



# Mission Code
mission_code = f"{agent_name[:3].upper()}{agent_age}{agent_favorite_color}"



# Boolean Expression
is_adult = agent_age >= 18

has_many_gadgets = agent_number_of_gadgets > 5

has_training = agent_training_years > 0



print("\n===========Mission Briefing:=============")
print("\n")
print(f"Agent Name: {agent_name}")
print(f"Mission Code: {mission_code}")  
print ("\n")
print(f"Agent Age: {agent_age}")       
print(f"Agent Training Years: {agent_training_years}")
print(f"Training Percentage: {training_percentage:.2f}%")
print("\n")
print(f"Agent Favorite Color: {agent_favorite_color}")
print("\n")
print(f"Agent Number of Gadgets: {agent_number_of_gadgets}")
print(f"Gadget Density: {gadget_density:.2f} gadgets per year")
print("\n")
print (f"Mission Time: {mission_seconds} seconds")
print (f"Mission Time Remaining: {mission_seconds - 300} seconds")
print (f"Mission Time in Seconds: {mission_seconds} seconds")
print("\n")
print(f"Adult Agent: {is_adult}")
print(f"Many Gadgets: {has_many_gadgets}")

print(f"Training Experience: {has_training}")

print("\n==============Good luck on your mission, Agent " + agent_name + "!==============")