var rand = Math.floor((Math.random()*25)+1);
var imgCache = new Image();
imgCache.src = '/static/todoapp/css/images/stock' + rand + '.jpg';
$(window).on('load', function() {
    $("body").css({ "background": "url(/static/todoapp/css/images/stock" + rand + ".jpg)",
                   "background-size": "100% 100%",
                   "background-repeat": "no-repeat"
                  });
});

function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
    h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
  }

  function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
  }
  