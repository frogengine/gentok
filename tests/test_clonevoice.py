from libclonevoice import clonevoice

def test_clonevoice():
    assert clonevoice.clonevoice(
        "Hello Gentok",
        "D:\workspace\python\gentoklibs\sample-5.mp3"
    ) 