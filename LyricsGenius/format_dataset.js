var fs = require('fs');
var songs = JSON.parse(fs.readFileSync('Lyrics_Booba.json', 'utf8')).songs;

console.log(songs)

var formatedSongs = [];
for (var i = 0, l = songs.length; i < l; i++) {
	formatedSongs.push(songs[i].lyrics);
}


fs.writeFile("booba.txt", formatedSongs.join(" "), function(err) {
    if(err) {
        return console.log(err);
    }

    console.log("The file was saved!");
}); 

console.log(formatedSongs)

