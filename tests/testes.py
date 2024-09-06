import vaex
import time
import pandas as pd

arquivo = 'data/measurements.txt'

print("\033[32mIniciando o processamento do arquivo.\033[m")

start_time = time.time()

# df = vaex.from_csv(arquivo, names=['estacao', 'temperatura'], delimiter=';')  # 100M levou 18.08s

# df = vaex.read_csv(arquivo, names=['estacao', 'temperatura'], delimiter=';')  # 100M levou 17.50s

# df = vaex.from_csv(arquivo, names=['estacao', 'temperatura'], delimiter=';', convert=True)  # 100M levou 28.94s

df = vaex.from_csv(arquivo, names=['estacao', 'temperatura'], delimiter=';', convert=True)  # 1B levou 316.52s

# df = vaex.open('data/measurements100M.txt.hdf5')  # 100M levou 0.17s

# df = pd.read_csv(arquivo, names=['estacao', 'temperatura'], delimiter=';')  # 100M levou 13.70s

took = time.time() - start_time

print(df.head())

print(f"Processing took: \033[32m{took:.2f}\033[m sec")