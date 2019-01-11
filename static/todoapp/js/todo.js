//randomized background loading
var rand = Math.floor((Math.random()*25)+1);
var imgCache = new Image();
imgCache.src = '/static/todoapp/css/images/stock' + rand + '.jpg';
$(window).on('load', function() {
    $("body").css({ "background": "url(/static/todoapp/css/images/stock" + rand + ".jpg)",
    "background-size": "100% 100%",
    "background-repeat": "no-repeat"
    });
});

//function to keep track of time on the Today homepage
function startTime() {
    var today = new Date();
    var hour = today.getHours();
    var minute = today.getMinutes();
    var second = today.getSeconds();
    minute = checkTime(minute);
    second = checkTime(second);
    document.getElementById('txt').innerHTML =
    hour + ":" + minute + ":" + second;
    var t = setTimeout(startTime, 500);
  }

  //zero pad for numbers < 10
  function checkTime(i) {
    if (i < 10) {
        i = "0" + i};
    return i;
  }
  