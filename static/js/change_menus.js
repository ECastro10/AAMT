/**
 * Created by emanuel on 3/3/17.
//  */

function changeTheoryMenuItems() {
    $("#menu-content").empty();
    var theoryItems = $( "#theory-menu-content" ).find( "li" ).clone();
    theoryItems.each(function (index, value) {
        $("#menu-content").append(value);
    });

}

function changeMenuItems() {
    $("#menu-content").empty();
    var menuItems = $( "#main_menu" ).find( "li" ).clone();
    menuItems.each(function (index, value) {
        $("#menu-content").append(value);
    });

}