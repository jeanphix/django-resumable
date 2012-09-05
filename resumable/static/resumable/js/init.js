document.addEventListener("DOMContentLoaded", function () {
    "use strict";
    var dj;
    if (new Resumable().support) {
        dj = new DjangoResumable();
    }
});
