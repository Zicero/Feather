$("code").each(function() {
  var code = $(this);
  if (code.text().length > 50) {
    var button = $(`
      <pre style="text-align:right;">
        <div style="
              transform: translate(0px, 0px) scale(1);
              background-clip: content-box;
              cursor: pointer;
              background-image: url('https://files.slack.com/files-tmb/T0KK0T0RK-F6FHUCS7N-53a00141cf/webp.net-resizeimage__1__360.png');
              background-size: 100%;
              width: 22px;
              height: 22px;
              position: relative;
              text-align: center;
              color: rgb(255, 255, 255);
              transition: transform 0.25s ease-in-out, font 0.18s ease-out, background-image 0.25s ease-in-out, opacity 0.18s ease-in !important;
              border-radius: 100% !important;
              background-repeat: no-repeat !important;
              background-position: center center !important;
              font: 14px/22px 'Helvetica Neue', Lato !important;
              margin: 0px !important;
              padding: 0px !important;
              float: right;">
        </div>
        <code style="display:none;">
          ${code.text()}
        </code>
      </pre>`
    );
    button.bind("click", click);
    code.append(button);
  }
});

var app, editor;

function click() {
  const data = $($(this).find($('code')));
  chrome.runtime.sendMessage({
		location: window.location,
    code: {
      text: data.text()
    }
	});
  var div = $(`
    <div id="angelhack">
      <div m-if="loading" class="load">
         <div class="dot"></div>
         <div class="outline"><span></span></div>
      </div>
      <div id="modal" class="modal">
        <div class="modal-background"></div>
        <div style="background-color:white !important;" class="modal-content">
          <div id="editor">
            {{code}}
          </div>
        </div>
        <button style="box-shadow: none !important;" id="close" class="modal-close is-large"></button>
      </div>
    </div>
  `).appendTo('body');
  setTimeout(function () {
    $('#close').click(function () {
      $('.modal').removeClass('is-active');
    });
  }, 250);

  app = new Moon({
    el: "#angelhack",
    data: {
      loading: true,
      code: "Hello Moon!" //eventually request.data
    }
  });

  var options = {
    debug: 'info',
    modules: {
      toolbar: false
    },
    placeholder: '',
    readOnly: false,
    theme: 'snow'
  };
  var editor = new Quill('#editor', options);

  setTimeout(function (){
    app.set('loading', false);
    $('.modal').addClass('is-active');
  }, 3000)
}


// chrome.extension.onRequest.addListener(function(request, sender, sendResponse){

  // app.set('loading', false);
// }
