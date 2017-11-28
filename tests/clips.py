from random import choice
from pyknow import *
from pyknow.watchers import FACTS


class Light(Fact):
    """Info about the traffic light."""
    pass


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule('light' << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])
        # self.retract(light)



engine = RobotCrossStreet()
watch('FACTS', 'AGENDA')
engine.reset()
l = Light(color=choice(['green', 'yellow', 'blinking-yellow', 'red']))
engine.declare(l)
engine.run()
engine.modify(l, color='red')
engine.run()
print(engine.facts)
