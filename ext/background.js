chrome.extension.onMessage.addListener(function(message, sender, sendResponse){
  $.ajax({
		type: 'POST',
		url: '',
		crossDomain: true,
		data: JSON.stringify(message),
		contentType: 'application/json; charset=utf-8',
		dataType: 'json',
		async: false,
		success: function () {

		}
	});
});

// chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
//     chrome.tabs.sendMessage(tabs[0].id, {action: "open_dialog_box"}, function(response) {});
// });
