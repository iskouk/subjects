import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS

df = pd.read_csv('subjects.csv', index_col = '@id', keep_default_na = True, dtype = { 'pav:version': str })

namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('skos', SKOS, override = True)
namespace_manager.bind('iskouksubj', Namespace('https://iskouk.org/subjects/'), override = True)
namespace_manager.bind('pav', Namespace('http://purl.org/pav/'), override = True)

g = rdfpandas.to_graph(df, namespace_manager)

ttl = g.serialize(format = 'turtle')
with open('subjects.ttl', 'w') as file:
   file.write(ttl)
