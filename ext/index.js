$("code").each(function() {
  var code = $(this);
  if (code.text().length > 100) {
    var button = $(`
      <pre id="pre" style="
        text-align:right;
        margin-bottom: 0 !important;
        padding-bottom: 0px !important;
        ">
        <span class="nowrap">
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
        </span>
        <code style="display:none;">
          ${code.text()}
        </code>
      </pre>`
    );
    button.bind("click", click);
    code.append(button);
  }
});

var app, editor, output;

function click() {
  $('#angelhack').remove();
  const data = $($(this).find($('code')));
  chrome.runtime.sendMessage({
		location: window.location,
    code: {
      text: data.text()
      // text: data.text().replace('urlencode', 'fag')
    }
	}, function (data) {
    outputReceived(data);
  });
  var div = $(`
    <div id="angelhack">
      <div m-if="loading" class="load">
         <div class="dot"></div>
         <div class="outline"><span></span></div>
      </div>
      <div id="modal" class="modal">
        <div class="modal-background"></div>
        <div style="background-color:#FFFBFA !important; border: 4px solid #00d1b2; color: #363732 !important;" class="modal-content">
          <div class="content">
            <div class="columns">
              <div class="column is-half">
                <h3 class="title is-3">Code</h3>
                <div style="border: 1px solid #54DEFD;" class="box">
                  <div id="editor">
                    {{code}}
                  </div>
                </div>
                <center>
                  <a id="resend" class="button is-medium is-primary">Run</a>
                </center>
              </div>
              <div style="border-left: 1px solid #00d1b2;" class="column is-half">
                <h3 class="title is-3">Output</h3>
                <div id="outputBox" style="border: 1px solid #41b2f4;" class="box">
                  <div id="output">
                    {{output}}
                  </div>
                </div>
                <center>
                  <a id="expand" style="font-size: 2em; color: black !important; border-color: #FFFBFA !important; background-color: #FFFBFA !important; box-shadow:none !important;" class="button is-large">
                    ▼
                  </a>
                  <a id="despand" style="display: none; font-size: 2em; color: black !important; border-color: #FFFBFA !important; background-color: #FFFBFA !important; box-shadow:none !important;" class="button is-large">
                    ▲
                  </a>
                </center>
              </div>
            </div>
          </div>
          <div style="display:none;" id="analytics">
            <table class="table">
              <thead>
                <tr>
                  <th><abbr title="Language">Language</abbr></th>
                  <th><abbr title="Start Time">Start Time</abbr></th>
                  <th><abbr title="Run Time">Run Time</abbr></th>
                  <th><abbr title="Memory">Memory</abbr></th>
                </tr>
              </thead>
              <tbody>
                <tr>
                 <td>{{language}}</td>
                 <td>{{start_time}}</td>
                 <td>{{run_time}}</td>
                 <td>{{memory}}</td>
               </tr>
              </tbody>
            </table>
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
    $('#expand').click(function () {
      $('#analytics').show();
      $('#despand').show();
      $('#expand').hide();
      $('#table').show();
    });
    $('#despand').click(function () {
      $('#analytics').hide();
      $('#despand').hide()
      $('#expand').show();
      $('#table').hide();
    });
    $('#resend').click(function () {
      $('#langDetected').html('');
      $('#resend').addClass('is-loading');
      $('#despand').trigger('click');
      console.log($('#editor').text());

      chrome.runtime.sendMessage({
        location: window.location,
        code: {
          text: $('#editor').text()
        }
      }, function (data) {
        outputReceived(data);
        $('#resend').removeClass('is-loading');
      });
      $($('.ql-editor')[0]).find('*').remove();
      $($('.ql-editor')[1]).find('*').remove();
      $($('.ql-editor')[0]).append("<p></p>");
      $($('.ql-editor')[1]).append("<p></p>");

      $($('.ql-editor')[1]).children('p').html('');
    });
  }, 250);

  app = new Moon({
    el: "#angelhack",
    data: {
      loading: true,
      code: "Hello World!",
      language: '',
      start_time: '',
      run_time: '',
      memory: ''
    }
  });

  var editorOptions = {
    debug: false,
    modules: {
      toolbar: false
    },
    placeholder: '',
    readOnly: false,
    theme: 'snow'
  };
  var outputOptions ={
    debug: false,
    modules: {
      toolbar: false
    },
    placeholder: '',
    readOnly: true,
    theme: 'snow'
  }

  editor = new Quill('#editor', editorOptions);
  output = new Quill('#output', outputOptions);

  editor.on('text-change', function(delta, oldDelta, source) {
    app.set('output', $('#output').text());
  });

  editor.on('text-change', function(delta, oldDelta, source) {
    app.set('code', $('#editor').text());
  });
}

function outputReceived(request) {
  console.log(request);
  if (request) {
    if (request.error) {
      $($('.ql-editor')[0]).children('p').html(request.code);
      $($('.ql-editor')[1]).children('p').html(request.error);
      $('#outputBox').css('border', '1px solid #FF5E5B');
      $('#despand').trigger('click');
      app.set('language', '');
      app.set('run_time', '');
      app.set('memory', '');
      app.set('start_time', '');
    } else {
      $('#outputBox').css('border', '1px solid #41b2f4');
      app.set('code', request.code);
      app.set('output', request.output);
      app.set('language', request.analytics['Language Detected']);
      app.set('run_time', request.analytics['Runtime']);
      app.set('memory', request.analytics['Memory (CPU)']);
      app.set('start_time', request.analytics['Boot Time']);


      if (request.analytics) {
        $('#langDetected').html(request.analytics['Language Detected']);
      }

      $($('.ql-editor')[0]).children('p').html(request.code);
      $($('.ql-editor')[0]).children('p').css("font-weight","Bold");
      $($('.ql-editor')[1]).children('p').html(request.output);
      $($('.ql-editor')[1]).children('p').css("font-weight","Bold");

      if (request.output.toLowerCase().includes('error')) {
        $('#outputBox').css('border', '1px solid #FF5E5B');
      }
    }
    $('.modal').addClass('is-active');
    app.set('loading', false);
    $('.loading').remove();
  }
}
