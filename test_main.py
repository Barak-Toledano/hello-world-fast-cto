from main import say_hello

def test_output(capsys):
    say_hello()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, world!"