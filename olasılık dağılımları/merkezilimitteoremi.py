###MERKEZİ LİMİT TEOREMİ### 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
# okey
yas=np.random.uniform(low=18,high=70,size=30000)
orneklem=[np.mean(random.choices(yas,k=30)) for _ in range(1000)]
print(yas)
plt.hist(orneklem)
plt.show()
#buna benzer bir örneği aslında kendin excelde oluşturup böyle bir örneklem çekmelesin