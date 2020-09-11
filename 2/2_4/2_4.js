var fs = require('fs');
fs.readFile('input.txt', "utf8", function (err, data) {
    if (err) {
        console.error(err);
    } else {
        var str_ar = data.split(' ')
        var n = str_ar[0]
        var m = str_ar[1]
        n = Number(n)
        m = Number(m)
        n = n ** n
        var x = (n % m + m) % m
        console.log(x);
    }
});
