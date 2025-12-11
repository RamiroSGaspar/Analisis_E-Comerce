import numpy as np

# 1000 usuarios
np.random.seed(42)

# Funnel: 0=solo visitó, 1=vio productos, 2=agregó carrito, 3=compró
funnel = np.random.choice([0, 1, 2, 3], size=1000, p=[0.3, 0.35, 0.2, 0.15])

# Tipo usuario: 0=nuevo, 1=recurrente
tipo_usuario = np.random.choice([0, 1], size=1000, p=[0.6, 0.4])

# Monto gastado (solo para quienes compraron, resto es 0)
montos = np.where(funnel == 3, 
                  np.random.randint(20, 200, size=1000), 
                  0)