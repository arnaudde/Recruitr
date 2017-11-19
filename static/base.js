$(document).ready(function(){
	$(".nav.navbar-nav li").removeClass("active")
	if(loc=="applicants"){
		$("#li-applicants").addClass("active")
	}
	else if (loc=="home"){
		$("#li-home").addClass("active")
	}
	else {
		$("#li-positions").addClass("active")
	}
})
