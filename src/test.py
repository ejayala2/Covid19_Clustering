from SPARQLWrapper import SPARQLWrapper, JSON, CSV
import pandas as pd


sparql = SPARQLWrapper("http://localhost:7200/repositories/publications")

sparql.setQuery("""
 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX dcterms: <http://purl.org/dc/terms/>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX fabio: <http://purl.org/spar/fabio/>
PREFIX data: <http://utpl.edu.ec/lod/publicationsCOVID#>
PREFIX dbo: <http://dbpedia.org/ontology/>
SELECT ?Publicaciones ?DOI ?Titulo_Publicacion ?Autores ?Nombre_Revista ?Nombre_Organizacion ?Tipo_Licencia ?URL ?Fecha_Publicacion
WHERE{
    ?Publicaciones rdf:type dcterms:BibliographicResource .
    ?Publicaciones dcterms:title ?Titulo_Publicacion ;
    dcterms:license ?Licencia .
    ?Licencia foaf:name ?Tipo_Licencia .
    ?Publicaciones fabio:doi ?DOI .
   	?Publicaciones data:authors ?Autores .
	?Publicaciones dcterms:publisher ?Organizacion .
    ?Organizacion foaf:name ?Nombre_Organizacion .
    ?Publicaciones fabio:hasURL ?URL .
    ?Publicaciones dbo:AcademicJournal  ?Revista .
    ?Revista foaf:name ?Nombre_Revista .
    ?Publicaciones dcterms:date ?Fecha_Publicacion .
} ORDER BY(?Titulo_Publicacion)
""")
sparql.setReturnFormat(CSV)
results = sparql.query().convert()

# print(results)

# results_df = pd.io.json.json_normalize(results['results']['bindings'])
# results_df[['Publicaciones.value', 'DOI.value']].head()


for result in results["results"]["bindings"]:
    print(result)

# print(results.serialize(format='json'))