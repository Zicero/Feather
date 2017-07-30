chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
  $.ajax({
		type: 'POST',
		url: 'http://f8e15def.ngrok.io',
		crossDomain: true,
		data: JSON.stringify(message),
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		async: false,
		success: function (data) {
			console.log(data);
			data.whou = 'itme';
		  sendResponse(data);
		}
	});
});
