class Scene(object):

    def __init__(self):
        pass
        
    #choice = raw_input('\nMake your choice:\n>>> ') # standard prompt entry
        
    def enter(self, scene_name):
        pass

    def create_options(self, options):
        length = len(options) # calculates the number of options there are
        options_dict = {} # creates the dictionary that will store the numbered options
        
        for num in xrange(0, length): # iterates through the number of options
            options_dict[num + 1] = options[num] # creates the dictionary entry for each option
            
        return options_dict # returns the new dictionary
        
    def print_options(self, options_dict): # accepts a dictionary as an argument
        assert type(options_dict) == dict, "options_dict is not a dictionary:  %r" % options_dict
    
        for key, value in options_dict: # iterates through the dictionary
            print "%s:  %s" % (key, value)
        
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        opening_scene = self.scene_map.opening_scene()
            

class Death(Scene):

    def enter(self):
        pass

class Castle(Scene):

    def enter(self, first_time = True):
        pass

class KillerRabbit(Scene):

    def enter(self):
        pass

class BridgeOfDeath(Scene):

    def enter(self):
        pass
        
class Map(object):

    scenes = {
        'castle': Castle(),
        'killer_rabbit': KillerRabbit(),
        'bridge_of_death': BridgeOfDeath(),
        'death': Death(),
        }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        """Returns whatever class name is associated with the shorthand argument"""
        val = Map.scenes.get(scene_name)

        return val
        
    def opening_scene(self):
        """Returns the class name of whatever opening scene is set"""
        return self.next_scene(self.start_scene)
        
