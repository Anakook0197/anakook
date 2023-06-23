import pandas as pd
import mlxtend
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [['bread', 'milk', 'eggs'],
         ['bread', 'diapers', 'beer', 'eggs'],
         ['milk', 'diapers', 'beer', 'cola'],
         ['bread', 'milk', 'diapers', 'beer', 'cola'],
         ['bread', 'milk', 'diapers', 'beer']]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.6, use_colnames= True)

print(frequent_itemsets)






