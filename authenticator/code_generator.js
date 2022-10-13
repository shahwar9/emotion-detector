var today = new Date();

const codes = ["486920", "126907", "629548", "966924", "734434", "299446",
               "271511", "881089", "230065", "643689", "875066", "309194",
               "986766", "928893", "935513", "642307", "114531", "708926",
               "515063", "287081", "773087", "498614", "293744", "540712",
               "284162", "253386", "428445", "283243", "421294", "421294",
               "596150", "459160", "220646", "843279", "776503", "827386",
               "312314", "902189", "616912", "499444", "607877", "284338",
               "943144", "104613", "914061", "852121", "719881", "634124",
               "117705", "268263", "226969", "541811", "591931", "562221",
               "633878", "996298", "439396", "315797", "428380", "694293"]

function countdown() {
    var seconds = 10;

    var today = new Date();
    var minutes = today.getMinutes();
    document.getElementById("auth_code").innerHTML = codes[today.getSeconds()];

    function tick() {
        var counter = document.getElementById("counter");
        seconds--;
        counter.innerHTML = "0:" + (seconds < 10 ? "0" : "") + String(seconds);
        document.getElementById("auth_code").innerHTML = codes[seconds];
        if (seconds > 0) {
            setTimeout(tick, 1000);
        } else {
            countdown();
        }
    }
    tick();
}

countdown();