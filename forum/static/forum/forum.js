(function () {
  "use strict";

  function trimmedLength(value) {
    return (value || "").trim().length;
  }

  document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("plh-post-form");
    if (!form) {
      return;
    }

    const title = form.querySelector("input[name='title']");
    const content = form.querySelector("textarea[name='content']");
    const counter = document.getElementById("contentCount");

    function updateCounter() {
      if (content && counter) {
        counter.textContent = String(content.value.length);
      }
    }

    function applyCustomValidity() {
      if (title) {
        title.setCustomValidity(
          trimmedLength(title.value) >= 5 ? "" : "Title must be at least 5 characters."
        );
      }

      if (content) {
        content.setCustomValidity(
          trimmedLength(content.value) >= 20 ? "" : "Content must be at least 20 characters."
        );
      }

      updateCounter();
    }

    if (title) {
      title.addEventListener("input", applyCustomValidity);
    }

    if (content) {
      content.addEventListener("input", applyCustomValidity);
    }

    form.addEventListener(
      "submit",
      function (event) {
        applyCustomValidity();
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );

    applyCustomValidity();
  });
})();
