$(document).ready(
    
    function(){
    var searchTerm;
    $("#btnSearch").click(function() {
    searchTerm = "";
    if ($("#search").val() == "") {
    alert("You must enter one or more tags!"); }
    else {
    searchTerm = $("#search").val();
    var url = "http://api.flickr.com/services/feeds/" +
    "photos_public.gne?format=json&jsoncallback=?" +
    "&tags=" + searchTerm + "&tagmode=all";
    $.getJSON(url, function(data){
    var html = "";
    
    $.each(data.items, function(i, item){
    var t="";
    //t+="<div class='results'>"
    t += "<h2>" + item.title + "</h2>";
    t += "<img src=" + item.media.m + ">";
    t += "<p><b>Tags: </b>" + item.tags + "</p>";
    t += "<hr> <br>";
    //t += "</ div>";
    html+=t;
    t="";
    });
    $("#photos").html(html);
    });
    }
    });
    }
    
    
    
    );