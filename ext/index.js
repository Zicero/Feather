$("code").each(function() {
  var code = $(this);
  if (code.text().length > 50) {
    var button = $(`
      <pre style="text-align:right;">
        <img src="http://placehold.it/50x50" id="wow">
        <code style="display:none;">
          ${code.text()}
        </code>
      </pre>`
    );
    button.bind("click", click);
    code.append(button);
  }
});

function click() {
  const data = $($(this).find($('code')));
  chrome.runtime.sendMessage({
    window: window,
		href: window.location.href,
    code: {
      text: data.text()
    }
	});
}


// chrome.extension.onRequest.addListener(function(request, sender, sendResponse){

  var div = $(`
      <div class="modal is-active">
        <div class="modal-background"></div>
        <div class="modal-content">
          <p class="image is-4by3">
            <img src="http://bulma.io/images/placeholders/1280x960.png">
          </p>
        </div>
        <button id="close" class="modal-close is-large"></button>
      </div>
  `).appendTo('body');

  $('#close').click(function () {
    $('.modal').removeClass('is-active');
  });

  const app = new Moon({
    el: "#angelhack",
    data: {
      msg: "Hello Moon!" //eventually request.data
    }
  });

  

// }
