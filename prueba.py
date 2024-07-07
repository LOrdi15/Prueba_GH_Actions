# Este es un simple script de Python para pruebas en GitHub Actions

def test_sum():
    assert sum([1, 2, 3]) == 6, "Debe ser 6"

def test_subtract():    
    assert subtract(5, 3) == 2, "Debe ser 2"

def subtract(a, b):
    return a - b



def write_to_file(filename, content):
    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    test_sum()
    test_subtract()
    print("Prueba exitosa")
    write_to_file('Test_Resultado.txt', 'Prueba exitosa')