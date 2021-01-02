
var InCHlib = require("../lib/inchlib-1.2.0");
var tet = require("../resources/microarrays.json")
export function drawmap(json){
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

inchlib.send_json(JSON.parse(json));
const res = document.getElementById("checkbox").checked;
if(res){
    var table = document.getElementById("table-box");
    table.style.display="none";
}
else{
    var table = document.getElementById("table-box");
    table.style.display="block";
}
inchlib.draw();
}
