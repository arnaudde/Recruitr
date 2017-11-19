$(document).ready(function(){

	jQuery('#id_datetime_begin').datetimepicker({
	  format:'Y-m-d H:i',
	  inline:true,
	  lang:'en'
	});
	jQuery('#id_datetime_end').datetimepicker({
	  format:'Y-m-d H:i',
	  inline:true,
	  lang:'en'
	});
	console.log(success)
	if(success=="True"){

		$(".form").hide()
		$(".answer").show()
	}
})