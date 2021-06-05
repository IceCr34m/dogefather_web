'use strict';
$(document).ready(function () {
  new Animate({
    target: '[data-animate]',
    offset: [0.2, 0.5],
    delay: 0,
    remove: false,
    reverse: true,
    scrolled: true,
    debug: true,
    onLoad: true,
    onScroll: true,
    onResize: true,
  }).init();

  const clipboardBsc = new ClipboardJS('.bsc.copy-to-clipboard i');
  clipboardBsc.on('success', function (e) {
    $('.address .bsc i strong').html('Copied!');
    setTimeout(function () {
      $('.address .bsc i strong').html('Copy');
    }, 3000);

    e.clearSelection();
  });

  if (!ClipboardJS.isSupported()) {
    $('.fold .address a i').hide();
  }

  $('.nfts-carousel').owlCarousel({
    loop: true,
    nav: false,
    margin: 30,
    autoplay: true,
    autoplayTimeout: 5e3,
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1,
      },
      480: {
        items: 2,
      },
      575: {
        items: 3,
      },
      991: {
        items: 4,
      },
    },
  });

  $(window).on('scroll', () => {
    if ($(this).scrollTop() > 400) {
      $('.scroll-to-top').addClass('show');
    } else {
      $('.scroll-to-top').removeClass('show');
    }
  });
  $('.scroll-to-top').on('click', () => {
    return (
      $('.scroll-to-top').tooltip('hide'),
      $('body,html').animate(
        {
          scrollTop: 0,
        },
        2e3
      ),
      false
    );
  });

  /* $('a.nav-link').on('click', function (event) {
    if ("" !== this.hash && window.href.split('/').pop(-1) === window.pathname) {
      event.preventDefault();
      var target = this.hash;
      $('html, body').animate(
        {
          scrollTop: $(target).offset().top,
        },
        800,
        function () {
          window.location.hash = target;
        }
      );
    }
    return;
  }); */
  
  $(window).on('load', () => {
    $('#preloader').delay(700).fadeOut(500);
  });
});

$('.navbar-nav>li>a').on('click', function() {
  $('.navbar-collapse').collapse('hide');
});

function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en'}, 'google_translate_element');
}
