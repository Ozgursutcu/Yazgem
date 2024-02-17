

import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000) # Normal dağılıma sahip rastgele veri üret

plt.hist(data, bins=30) # Histogramı çiz
plt.title('Histogram')
plt.xlabel('Değerler')
plt.ylabel('Sıklık')
plt.show()
