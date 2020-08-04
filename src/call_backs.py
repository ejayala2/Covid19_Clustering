from bokeh.models import CustomJS

# handle the currently selected article
def selected_code():
    code = """
            var uris= [];
            var dois= [];
            var titulos= [];
            var autores = [];
            var fechas = [];
            var revistas = [];
            var organizaciones = [];
            var licencias = [];
            urls = [];

            cb_data.source.selected.indices.forEach(index => uris.push(source.data['Uri_Pb'][index]));
            cb_data.source.selected.indices.forEach(index => dois.push(source.data['Doi'][index]));
            cb_data.source.selected.indices.forEach(index => titulos.push(source.data['Titulo'][index]));
            cb_data.source.selected.indices.forEach(index => autores.push(source.data['Autores'][index]));
            cb_data.source.selected.indices.forEach(index => fechas.push(source.data['Fecha'][index]));
            cb_data.source.selected.indices.forEach(index => revistas.push(source.data['Revista'][index]));
            cb_data.source.selected.indices.forEach(index => organizaciones.push(source.data['Organizacion'][index]));
            cb_data.source.selected.indices.forEach(index => licencias.push(source.data['Licencia'][index]));
            cb_data.source.selected.indices.forEach(index => urls.push(source.data['URL'][index]));
            
            title = "<h4>" + titulos[0].toString().replace(/<br>/g, ' ') + "</h4>";
            authors = "<p1><b>Autores:</b> " + autores[0].toString().replace(/<br>/g, ' ') + "<br>"
            // journal = "<b>Revista</b>" + revistas[0].toString() + "<br>"
            link = "<b>DOI:</b> <a href='" + "http://doi.org/" + dois[0].toString() + "'>" + "http://doi.org/" + dois[0].toString() + "</a></p1>"
            current_selection.text = title + authors + link
            current_selection.change.emit();
    """
    return code

# handle the keywords and search
def input_callback(plot, source, out_text, topics): 

    # slider call back for cluster selection
    callback = CustomJS(args=dict(p=plot, source=source, out_text=out_text, topics=topics), code="""
				var key = text.value;
				key = key.toLowerCase();
				var cluster = slider.value;
                var data = source.data; 
                
                
                x = data['x'];
                y = data['y'];
                x_backup = data['x_backup'];
                y_backup = data['y_backup'];
                labels = data['desc'];
                titulos = data['titulo'];
                autores = data['autores'];
                revista = data['revista'];
                if (cluster == '3') {
                    out_text.text = 'Keywords: Slide to specific cluster to see the keywords.';
                    for (i = 0; i < x.length; i++) {
						if( titulos[i].includes(key) || 
						autores[i].includes(key) || 
						revista[i].includes(key)) {
							x[i] = x_backup[i];
							y[i] = y_backup[i];
						} else {
							x[i] = undefined;
							y[i] = undefined;
						}
                    }
                }
                else {
                    out_text.text = 'Keywords: ' + topics[Number(cluster)];
                    for (i = 0; i < x.length; i++) {
                        if(labels[i] == cluster) {
							if(titulos[i].includes(key) || 
							autores[i].includes(key) || 
							revista[i].includes(key)) {
								x[i] = x_backup[i];
								y[i] = y_backup[i];
							} else {
								x[i] = undefined;
								y[i] = undefined;
							}
                        } else {
                            x[i] = undefined;
                            y[i] = undefined;
                        }
                    }
                }
            source.change.emit();
            """)
    return callback