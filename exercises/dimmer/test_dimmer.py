from exercises.dimmer.dimmer import Dimmer, Lamp


def test_should_return_lamp_consumption():
    dimmer = Dimmer(0, 100)
    watts = 10, 20
    for watt in watts:
        dimmer.add_lamp(Lamp(watt))
    dimmer.power(10)
    assert dimmer.consumption == 3
