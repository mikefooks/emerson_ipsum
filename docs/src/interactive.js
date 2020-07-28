(function (window, document, undefined) {
    let sampleTextEl = document.querySelector("#generated-text");
    let generateButton = document.querySelector("#generate");

    let paras = document.querySelector("#para-count");
    let sentences = document.querySelector("#sentence-count");

    function queryParams () {
        let p = paras.value;
        let s = sentences.value;
        return "?paras=" + p + "&sentences=" + s;
    }

    function refreshGenText () {
        let xhr = new XMLHttpRequest();
        xhr.open("GET", "http://localhost:8000" + queryParams());
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
    window.addEventListener("load", refreshGenText);

}).call(this, window, document);
