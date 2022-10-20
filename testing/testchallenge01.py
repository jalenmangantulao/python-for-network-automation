#!/usr/bin/python3

def hi(p="World"):
    return f'Hello {p}'

def test_hi():
    assert hi("Mars") == "Hello Mars"

def test_hi_fail():
    assert hi("Pluto") == "Hello World"
