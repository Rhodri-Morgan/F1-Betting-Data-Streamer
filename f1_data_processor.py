import os
import json


class F1DataProcessor:
    def __init__(self): 
        self.world_drivers_champion_json = os.path.join(os.getcwd(), 'historic_data/world_drivers_champion.json')

    def save_world_drivers_champion_data(self, world_drivers_champion_probabilities):
        ''' Saves world drivers champion probability data to JSON file in historic_data directory '''
        if not os.path.exists(self.world_drivers_champion_json):
            with open(self.world_drivers_champion_json, 'w') as f:
                json.dump(world_drivers_champion_probabilities, f)
        else:
            with open(self.world_drivers_champion_json) as f:
                world_drivers_champion_data = json.load(f)
            world_drivers_champion_merged = {**world_drivers_champion_data, **world_drivers_champion_probabilities}
            with open(self.world_drivers_champion_json, "w") as f:
                json.dump(world_drivers_champion_merged, f)
