
var InCHlib = require("../lib/inchlib-1.2.0");
// var tet = require("../resources/microarrays.json")
export function drawmap(json,target){
var inchlib = new InCHlib({"target": target,
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
var table = document.getElementById("table-box-connect-1to2");
var h1 = document.getElementById("headline1");
table.style.display="block";
h1.style.display="block";
if(!res){
    var table21 = document.getElementById("table-box-connect-2to1");
    var h2 = document.getElementById("headline2");
    h2.style.display="block";
    table21.style.display="block";
}
inchlib.draw();
};


export function drawmap2(json,target){
    var inchlib2 = new InCHlib({"target": target,
                        "width": 800,
                        "height": 1200,
                        "column_metadata_colors": "RdLrBu",
                        "heatmap_colors": "RdBkGr",
                        "max_percentile": 90,
                        "middle_percentile": 60,
                        "min_percentile": 10,
                        "heatmap_font_color": "white",
                         text: 'biojs'});
    
    inchlib2.send_json(JSON.parse(json));
    inchlib2.draw();
    }