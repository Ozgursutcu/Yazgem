

import matplotlib.pyplot as plt

labels = ['Parça A', 'Parça B', 'Parça C', 'Parça D']
sizes = [25, 35, 20, 20] # Her parçanın oranı

plt.pie(sizes, labels=labels, autopct='%1.1f%%') # Pasta grafiği çiz
plt.axis('equal') # Grafiği dairesel yap
plt.title('Pasta Grafiği')
plt.show()
