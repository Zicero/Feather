chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
  $.ajax({
		type: 'POST',
		url: 'http://3d3bb348.ngrok.io',
		crossDomain: true,
		data: JSON.stringify(message),
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		async: false,
		success: function (data) {
			console.log(data);
			data.whou = 'itme';
		  sendResponse(data);
		},
    error: function (data) {
			data.error = data.statusText;
      sendResponse(data);
    }
	});
});
