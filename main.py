'''
Program pobiera pliki z folderu input (mogą być różnych formatów)
Pyta się użytkownika na jaki format chce je przekonwertować
Konwertuje wszystkie pliki na ten format i zapisuje je do folderu output

Obsługiwane formaty: CSV, XML, JSON, YAML, TOML

folder readers -> pliki zajmujące się odczytem plików wejściowych i przetwarzających ich dane na typ dict
folder writers -> pliki przyjmujące dane typu dict i przetwarzające je na format wyjściowy
folder converters -> pliki spinające readery i writery i grupujące je pod kątem formatu wejściowego
'''