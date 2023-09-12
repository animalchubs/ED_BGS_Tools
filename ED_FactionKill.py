import json

# Define your faction and journal log file path
your_faction = "HIP 24947 Gold Mafia"  # Replace with your faction's name
log_file_path = "C:\\Users\\segegagn\\Saved Games\\Elite Dangerous\\Journal.2023-01-23T154450.01.log"  # Replace with the actual path to your journal log file

# Initialize a variable to store the total rewardcls
total_reward = 0

# Read and process the journal log file
with open(log_file_path, 'r', encoding='utf-8') as log_file:
    for line in log_file:
        try:
            log_entry = json.loads(line)
            if "event" in log_entry and log_entry["event"] == "Bounty":
                if log_entry.get("VictimFaction") == your_faction:
                    reward = log_entry.get("TotalReward", 0)
                    total_reward += reward
        except json.JSONDecodeError:
            pass  # Ignore lines that are not valid JSON

# Display the total reward for your faction
print(f"Total Reward for {your_faction}: {total_reward}")