$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect:'bounceIn',
        },
        out:{
            effect:'bounceOut',
        },
    })
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: 1,
        speed: "0.30",
        autostart:true
      });
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect:'fadeInUp',
            sync: true
        },
        out:{
            effect:'fadeOutUp',
            sync: true

        },
    })
    $("#MicBtn").click(function () { 
        eel.playAssistantSound();
        $("#oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommand()();
    });

    function doc_keyUp(e) {

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommand()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message) {

        if (message != "") {

            $("#oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommand(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#sendBtn").attr('hidden', true);

        }

    }

    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#sendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#sendBtn").attr('hidden', false);
        }
    }

    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    $("#sendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    

    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });
    eel.expose(showHood);
    function showHood() {
        $("#SiriWave").attr("hidden", true);
        $("#Oval").attr("hidden", false);
    }

});