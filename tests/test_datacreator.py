from benchmarking.datacreator import RealWorldData
from benchmarking.datacreator import first_name, last_name, power, effect


def test_default_values():
    d1 = RealWorldData(first_name=first_name(), last_name=last_name(), power=power(), effect=effect())
    d2 = RealWorldData(first_name=first_name(), last_name=last_name(), power=power(), effect=effect())
    
    e1, e2 = d1.effect, d2.effect
    p1, p2 = d1.power, d2.power
    
    assert (d1 > d2) == (e1*p1 > e2*p2)
    
    
    
def test_manual_values():
    d1 = RealWorldData(first_name='Tantradnya', last_name='Designs', power=99, effect=0.95)
    d2 = RealWorldData(first_name='Radantray', last_name='Powers', power=0.86, effect=0.50)
    
    assert d1 > d2
    assert d1 != d2