(function (window, document, undefined) {
    let sampleTextEl = document.querySelector("#generated-text");
    let generateButton = document.querySelector("#generate");

    let paraSlider = document.querySelector("#para-count");
    let sentSlider = document.querySelector("#sentence-count");

    let paraCounter = document.querySelector("#para-value");
    let sentCounter = document.querySelector("#sentence-value");

    function queryParams () {
        let p = paraSlider.value;
        let s = sentSlider.value;
        return "?paras=" + p + "&sentences=" + s;
    }

    function refreshValueCounters () {
        let p = paraSlider.value;
        let s = sentSlider.value;

        paraCounter.innerText = p;
        sentCounter.innerText = s;
    }

    function refreshGenText () {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "https://mikefooks.com/emerson/api" + queryParams());
        xhr.onload = function () {
            if (xhr.status == 200) {
                sampleTextEl.innerHTML = "";
                let response = JSON.parse(xhr.responseText).data;

                let newEls = response.map(function (p) {
                    let el = document.createElement("p");
                    el.innerText = p;
                    return el;
                });

                newEls.forEach(function (el) {
                    sampleTextEl.appendChild(el);
                });
            }
        };

        xhr.send();
    }

    generateButton.addEventListener("click", refreshGenText);
    paraSlider.addEventListener("change", refreshValueCounters);
    sentSlider.addEventListener("change", refreshValueCounters);
    window.addEventListener("load", refreshGenText);
    window.addEventListener("load", refreshValueCounters);

}).call(this, window, document);
