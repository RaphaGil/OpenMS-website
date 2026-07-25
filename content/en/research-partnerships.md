---
title: Research Partnerships
hidePageTitle: true
hideShortcuts: true
sidebar: false
---

<section class="governance-section rp-include" id="partnerships-include" aria-labelledby="partnerships-include-title">
  <p class="rp-eyebrow">Collaborate</p>
  <h2 id="partnerships-include-title">Partnerships include:</h2>
  <ul class="rp-include__grid">
    <li class="rp-include__card">Joint grant proposals</li>
    <li class="rp-include__card">Consortium &amp; collaborative projects</li>
    <li class="rp-include__card">Workflow &amp; algorithm development</li>
    <li class="rp-include__card">Benchmarking studies</li>
    <li class="rp-include__card">Infrastructure &amp; sustainability initiatives</li>
  </ul>
</section>

<section class="governance-section governance-section--contrast rp-partners" id="our-partners" aria-labelledby="our-partners-title">
  <p class="rp-eyebrow">Community</p>
  <h2 id="our-partners-title">Our Partners</h2>
  <p>
    OpenMS is proud to partner with academic research groups, core facilities,
    national infrastructure, nonprofits and industry partners.
  </p>
  {{< partners >}}
</section>

<section class="governance-section research-partnerships-form" id="partnership-form" aria-labelledby="partnership-form-title">
  <p class="rp-eyebrow rp-eyebrow--inverse">Get in touch</p>
  <h2 id="partnership-form-title">Tell us about your idea</h2>
  <div class="research-partnerships-form__body" aria-label="Partnership inquiry form">
    <iframe
      class="research-partnerships-form__tally-iframe"
      data-tally-src="https://tally.so/embed/gD1o0M?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
      loading="lazy"
      width="100%"
      height="484"
      frameborder="0"
      marginheight="0"
      marginwidth="0"
      title="Partnership Inquiry"
    ></iframe>
  </div>
  <script async src="https://tally.so/widgets/embed.js"></script>
  <script>
  (function () {
    function loadTallyEmbeds() {
      if (typeof window.Tally !== "undefined") {
        window.Tally.loadEmbeds();
        return;
      }
      document.querySelectorAll("iframe[data-tally-src]:not([src])").forEach(function (iframe) {
        iframe.src = iframe.dataset.tallySrc;
      });
    }
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", loadTallyEmbeds);
    } else {
      loadTallyEmbeds();
    }
  })();
  </script>
</section>
