
var InCHlib = require("../lib/inchlib-1.2.0");

export function drawmap(json){
console.log("second lvl" + json)
var inchlib = new InCHlib({"target": "inchlib",
                    "width": 800,
                    "height": 1200,
                    "column_metadata_colors": "RdLrBu",
                    "heatmap_colors": "RdBkGr",
                    "max_percentile": 90,
                    "middle_percentile": 60,
                    "min_percentile": 10,
                    "heatmap_font_color": "white",
                     text: 'biojs'});


inchlib.send_json(json);
inchlib.draw();
}