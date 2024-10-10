from encriptacion_mensaje import encriptacion_mensaje

def test_encriptacion_mensaje():
    assert encriptacion_mensaje('hola',0)=='hola'

def test_encriptacion_mensaje2():
    assert encriptacion_mensaje('abcd',1)=='bcde'