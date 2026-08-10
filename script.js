window.addEventListener("pageshow", function () {
  document.body.classList.add("page-ready");
  document.body.classList.remove("page-leaving");
});

document.addEventListener("DOMContentLoaded", function () {
  document.body.classList.add("page-ready");

  document.addEventListener("click", function (event) {
    var link = event.target.closest("a[href]");

    if (!link) {
      return;
    }

    var href = link.getAttribute("href");

    if (
      !href ||
      href.startsWith("#") ||
      href.startsWith("mailto:") ||
      href.startsWith("tel:") ||
      href.startsWith("sms:") ||
      href.startsWith("javascript:") ||
      link.target === "_blank" ||
      link.hasAttribute("download") ||
      event.defaultPrevented ||
      event.metaKey ||
      event.ctrlKey ||
      event.shiftKey ||
      event.altKey ||
      event.button !== 0
    ) {
      return;
    }

    var destination = new URL(link.href, window.location.href);

    if (destination.origin !== window.location.origin) {
      return;
    }

    if (
      destination.pathname === window.location.pathname &&
      destination.hash === window.location.hash
    ) {
      return;
    }

    event.preventDefault();
    document.body.classList.remove("page-ready");
    document.body.classList.add("page-leaving");

    window.setTimeout(function () {
      window.location.href = destination.href;
    }, 180);
  });
});