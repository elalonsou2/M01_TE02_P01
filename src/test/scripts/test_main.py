import os
import sys
import mock

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../../')
import src.main.scripts.main as main


def test_pedir_valor_palabra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Gato")
    assert main.pedir_valor("prueba", "palabra") == "Gato"


def test_pedir_valor_palabra_error(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "El Gato come")
    monkeypatch.setattr('builtins.input', lambda _: "Gato")
    assert main.pedir_valor("prueba", "palabra") == "Gato"


def test_pedir_valor_frase(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "El gato come")
    assert main.pedir_valor("prueba", "frase") == "El gato come"


def test_pedir_valor_letra(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "a")
    assert main.pedir_valor("prueba", "letra") == "a"


def test_pedir_valor_letra_2(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "H")
    assert main.pedir_valor("prueba", "letra") == "H"


def test_pedir_valor_letra_numero(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 97)
    assert main.pedir_valor("prueba", "numero") == 97


def test_tratar_letra_encontrada(letra_insertada = "a"
                                 ):
    # letra_insertada = "a"
    frase_partida = [['e', 'l'], ['g', 'a', 't', 'o'], ['c', 'o', 'm', 'e']]
    letras_adivinadas_resultado = [['+', '+'], ['+', 'a', '+', '+'],
                                   ['+', '+', '+', '+']]
    letras_adivinadas_original = [['+', '+'], ['+', '+', '+', '+'],
                                  ['+', '+', '+', '+']]
    main.tratar_letra_encontrada(letra_insertada, frase_partida,
                                 letras_adivinadas_original)
    assert letras_adivinadas_original == letras_adivinadas_resultado


def test_tratar_letra_encontrada():
    frase = "El gato come"
    letras_adivinadas_resultado = [['+', '+'], ['+', '+', '+', '+'],
                                   ['+', '+', '+', '+']]
    frase_partida_resultado = [['E', 'l'], ['g', 'a', 't', 'o'],
                               ['c', 'o', 'm', 'e']]

    letras_adivinadas = []
    frase_partida = []
    main.generar_letras_adivinadas_frase_partida(frase, letras_adivinadas,
                                                 frase_partida)
    assert letras_adivinadas_resultado == letras_adivinadas
    assert frase_partida_resultado == frase_partida


def test_jugar(monkeypatch):
    respuestas = iter(["el gato come", 99, 3, "0", "el gato come"])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    assert main.jugar() == 1


def test_dame_cadena_concatenada():
    assert main.dame_cadena_concatenada(["hola", "cocacola"], ", ") \
           == "hola, cocacola"


def test_jugar2(monkeypatch):
    respuestas = iter(["el perro ladra", 4, 6, 3, "2", "a", "0", "el perro "
                                                                 "ladra"])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    assert main.jugar() == 1


def test_jugar_error(monkeypatch):
    respuestas = iter(["el perro ladra", 2, 1, 3])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    assert main.jugar() == 0


def test_jugar_error2(monkeypatch):
    respuestas = iter(["la ventana es alta", 3, 4, "1", "alta", "2", "x"])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    assert main.jugar() == 0


def test_jugar3(monkeypatch):
    respuestas = iter(["la casa", 40, 3, 2, "2", "a", "2", "x", "1", "molino",
                       "1", "casa", "0", "ma casa", "0", "la casa"])
    monkeypatch.setattr('builtins.input', lambda _: next(respuestas))
    assert main.jugar() == 1
