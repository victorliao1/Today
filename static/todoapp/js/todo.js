var rand = Math.floor((Math.random()*25)+1);
var imgCache = new Image();
imgCache.src = '/static/todoapp/css/images/stock' + rand + '.jpg';
$(window).on('load', function() {
    $("body").css({ "background": "url(/static/todoapp/css/images/stock" + rand + ".jpg)",
                   "background-size": "100% 100%",
                   "background-repeat": "no-repeat"
                  });
});
