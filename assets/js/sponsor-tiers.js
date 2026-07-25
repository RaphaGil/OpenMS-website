(function () {
  "use strict";

  var root = document.querySelector("[data-sponsor-tiers]");
  if (!root) return;

  var toggles = Array.prototype.slice.call(
    root.querySelectorAll("[data-sponsor-tier]")
  );
  var panels = Array.prototype.slice.call(
    root.querySelectorAll("[data-sponsor-benefits]")
  );
  if (!toggles.length || !panels.length) return;

  function activate(tierId) {
    panels.forEach(function (panel) {
      var match = panel.getAttribute("data-sponsor-benefits") === tierId;
      panel.hidden = !match;
    });
    toggles.forEach(function (toggle) {
      var match = toggle.getAttribute("data-sponsor-tier") === tierId;
      toggle.setAttribute("aria-expanded", match ? "true" : "false");
      toggle
        .closest(".sponsor-tier")
        .classList.toggle("sponsor-tier--active", match);
    });
  }

  toggles.forEach(function (toggle) {
    toggle.addEventListener("click", function () {
      activate(toggle.getAttribute("data-sponsor-tier"));
      var panel = document.getElementById(
        "sponsor-benefits-" + toggle.getAttribute("data-sponsor-tier")
      );
      if (panel) {
        panel.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    });
  });

  activate(toggles[0].getAttribute("data-sponsor-tier"));
})();
