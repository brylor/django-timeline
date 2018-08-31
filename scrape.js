var request = require('request');
var cheerio = require('cheerio');
cheerioTableparser = require('cheerio-tableparser');
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./db.sqlite3', (err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Connected to the SQlite database.');
});


request('https://en.wikipedia.org/wiki/Timeline_of_United_States_history', function (error, response, html) {
  if (!error && response.statusCode == 200) {
    var $ = cheerio.load(html);
    $('.wikitable').each(function(){
      cheerioTableparser($);
      data = $("table").parsetable(true,true,true);

    });

    var c = data[0].map(function(e, i) {
    // ['year','date','event']
    //return [e, data[1][i],data[2][i]];
      // year, year, event, julien_start, julien_end, end_month, start_month,start_day
      return [e, e,data[2][i],'AD','AD',1,1,1];
  });

//   var fs = require('fs');
//   fs.writeFile("/tmp/test", c, function(err) {
//     if(err) {
//         return console.log(err);
//     }
//
//     console.log("The file was saved!");
// });
  //console.log(c)
  for (var i = 0, len = c.length; i < len; i++) {
    console.log(c[i]);
    db.run('INSERT INTO events_event(start_year,end_year,title,julian_start,julian_end,end_month,start_month,start_day) VALUES(?,?,?,?,?,?,?,?)', c[i], (err) => {
    	if(err) {
    		return console.log(err.message);
    	}
    	console.log('Row was added to the table: ${this.lastID}');
      })
};


  db.close((err) => {
  if (err) {
    return console.error(err.message);
  }
  console.log('Close the database connection.');
});
  }
});
