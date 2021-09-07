try:
    # Преднамеренно бросить исключение.
    raise Exception('I learn Python!')
except:
    print("Entered in except.")
    # Возобновить исключение.
    raise

