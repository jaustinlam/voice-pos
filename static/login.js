$( document ).ready(function(){
	$(".button-collapse").sideNav();
	// Number buttons for login
    $(".login-button").click(function(){
        var pText = $("#passcode_text").val();
        var bText = $(this).text();
        if(pText.length <= 3){
        	$("#passcode_text").val(pText + bText);
        	console.log($(this).text());
        } else {
        	$("#passcode_text").val(pText);
        };
    });
    // Clear login section
    $(".login-clear").click(function(){
    	$("#passcode_text").val("")
    });
    // Back space on login section
    $(".login-back").click(function(){
    	var pText = $("#passcode_text").val();
    	$("#passcode_text").val(pText.substring(0, pText.length-1))
    });




});

